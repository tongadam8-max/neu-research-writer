import os
import sys
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from bs4 import BeautifulSoup
import markdown

def clean_latex_and_text(text):
    mapping = {
        r'$\beta$': 'β', r'$p$': 'p', r'$t$': 't', r'$R^2$': 'R²', r'$f^2$': 'f²',
        r'$\alpha$': 'α', r'$\rho$': 'ρ', r'$\rightarrow$': '→', r'$\times$': 'x',
        r'$N$': 'N', r'$100\%$': '100%', r'$\le$': '≤', r'$\ge$': '≥',
        r'\beta': 'β', r'\rightarrow': '→', r'\times': 'x', r'\alpha': 'α',
        '—': '-'
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    text = text.replace('$', '')
    
    # 2. Xóa gạch đầu dòng/chấm tròn/số thứ tự do AI lỡ sinh ra
    text = re.sub(r'^\s*[-•\d\.]+\s*', '', text)
    
    # 3. Ép chuẩn Smart Quotes
    text = re.sub(r'"([^"]*)"', r'“\1”', text)
    text = re.sub(r"(^|\s)'([^']*)'(?=\s|[.,;:!?]|$)", r'\1“\2”', text)

    # 4. BỘ LỌC CỞI TRÓI NGOẶC KÉP CHO THUẬT NGỮ VÀ ẨN DỤ
    # Tháo ngoặc kép đối với các cụm từ ngắn (dưới 7 từ) để xóa dấu vết AI
    def unquote_short_phrases(match):
        content = match.group(1)
        word_count = len(content.split())
        if word_count <= 6:
            return content  # Trả về nội dung không có ngoặc
        return match.group(0) # Giữ nguyên ngoặc nếu là câu dài

    text = re.sub(r'“([^”]+)”', unquote_short_phrases, text)

    return text.strip()

def create_neu_standard_doc(input_folder, output_file="BaoCaoTongKet.docx"):
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.5)
        section.right_margin = Cm(2.0)

    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(13)
    style.paragraph_format.line_spacing = 1.5
    style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    if not os.path.exists(input_folder):
        print(f"Không tìm thấy thư mục {input_folder}")
        return

    all_md = sorted([f for f in os.listdir(input_folder) if f.endswith('.md')])
    md_files = [f for f in all_md if not f.startswith('test-')]
    if not md_files:
        md_files = all_md
    
    for md_file in md_files:
        with open(os.path.join(input_folder, md_file), 'r', encoding='utf-8') as f:
            content = f.read()
            
            # CÀN QUÉT ĐỒ THỊ ASCII
            content = re.sub(r'```.*?```', '\n[CHÈN HÌNH ẢNH ĐỒ THỊ TỪ PHẦN MỀM VÀO ĐÂY]\n', content, flags=re.DOTALL)
            content = re.sub(r'(?:[ /\|+-]{3,}\n){2,}', '\n[CHÈN HÌNH ẢNH ĐỒ THỊ TỪ PHẦN MỀM VÀO ĐÂY]\n', content)

            html = markdown.markdown(content, extensions=['tables'])
            soup = BeautifulSoup(html, 'html.parser')
            
            for element in soup:
                if element.name in ['h1', 'h2', 'h3', 'h4']:
                    level = int(element.name[1])
                    heading = doc.add_heading(clean_latex_and_text(element.text), level=level)
                    for run in heading.runs:
                        run.font.name = 'Times New Roman'
                        run.font.color.rgb = RGBColor(0, 0, 0)
                        if level == 1: run.font.size = Pt(16)
                        elif level == 2: run.font.size = Pt(14)
                        else: run.font.size = Pt(13)
                    heading.paragraph_format.first_line_indent = Cm(0)
                
                elif element.name in ['p', 'ul', 'ol']:
                    raw_lines = []
                    if element.name in ['ul', 'ol']:
                        for li in element.find_all('li'):
                            raw_lines.extend(clean_latex_and_text(li.text).split('\n'))
                    else:
                        raw_lines = clean_latex_and_text(element.text).split('\n')

                    for line in raw_lines:
                        line = line.strip()
                        if not line: continue
                        
                        if "CHÈN HÌNH ẢNH ĐỒ THỊ" in line:
                            p = doc.add_paragraph("[CHÈN HÌNH ẢNH ĐỒ THỊ TỪ PHẦN MỀM VÀO ĐÂY]")
                            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            p.paragraph_format.first_line_indent = Cm(0)
                            for run in p.runs:
                                run.font.italic = True
                                run.font.color.rgb = RGBColor(0, 0, 255)
                        else:
                            p = doc.add_paragraph(line)
                            p.paragraph_format.first_line_indent = Cm(1.27)
                
                elif element.name == 'table':
                    rows = element.find_all('tr')
                    if not rows: continue
                    cols = max(len(r.find_all(['th', 'td'])) for r in rows)
                    table = doc.add_table(rows=len(rows), cols=cols)
                    table.style = 'Table Grid'
                    for r_idx, row in enumerate(rows):
                        cells = row.find_all(['th', 'td'])
                        for c_idx, cell in enumerate(cells):
                            tc = table.cell(r_idx, c_idx)
                            tc.text = clean_latex_and_text(cell.text)
                            for paragraph in tc.paragraphs:
                                paragraph.paragraph_format.first_line_indent = Cm(0)
                            if cell.name == 'th':
                                for paragraph in tc.paragraphs:
                                    for run in paragraph.runs:
                                        run.font.bold = True
                                        
            doc.add_page_break()

    doc.save(output_file)
    print(f"Đã xuất thành công báo cáo chuẩn NEU ra file: {output_file}")

if __name__ == "__main__":
    draft_dir = sys.argv[1] if len(sys.argv) > 1 else "drafts"
    create_neu_standard_doc(draft_dir)
