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
        r'\%': '%',
        '—': '-'
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    text = text.replace('$', '')
    
    # Chuyển đổi số mũ toán học R^2, f^2, ^3
    text = text.replace('^2', '²').replace('^3', '³')
    
    # Ép chuẩn Smart Quotes
    text = re.sub(r'"([^"]*)"', r'“\1”', text)
    text = re.sub(r"(^|\s)'([^']*)'(?=\s|[.,;:!?]|$)", r'\1“\2”', text)

    # Chỉ gỡ bỏ ngoặc kép ở các thuật ngữ chuyên môn và ẩn dụ bị cấm theo QA Gate
    banned_terms = [
        r'Mua trước trả sau', r'Hiểu biết tài chính', r'Mua sắm bốc đồng',
        r'chiếc phanh', r'chiếc phanh nhận thức', r'nỗi đau thanh toán',
        r'không ma sát', r'hệ thống phản chiếu', r'hệ thống bốc đồng'
    ]
    for term in banned_terms:
        text = re.sub(rf'[“"\'‘](?i:{term})[”"\'’]', lambda m: m.group(0)[1:-1], text)

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
            def replace_ascii_code_blocks(match):
                block = match.group(0)
                if re.search(r'[-|+/\\]{3,}', block):
                    return '\n[CHÈN HÌNH ẢNH ĐỒ THỊ TỪ PHẦN MỀM VÀO ĐÂY]\n'
                return ''

            content = re.sub(r'```.*?```', replace_ascii_code_blocks, content, flags=re.DOTALL)
            content = re.sub(r'(?:[ /\|+-]{3,}\n){2,}', '\n[CHÈN HÌNH ẢNH ĐỒ THỊ TỪ PHẦN MỀM VÀO ĐÂY]\n', content)

            html = markdown.markdown(content, extensions=['tables'])
            soup = BeautifulSoup(html, 'html.parser')
            
            is_in_reference_section = False
            ref_counter = 1

            for element in soup:
                if element.name in ['h1', 'h2', 'h3', 'h4']:
                    raw_title = clean_latex_and_text(element.text)
                    
                    # Bỏ qua tiêu đề phân nhóm PHẦN KẾT nếu có để tránh tạo trang trắng mồ côi
                    if "PHẦN KẾT" in raw_title.upper() and element.name == 'h1':
                        continue

                    # Bắt tiêu đề TÀI LIỆU THAM KHẢO
                    if "TÀI LIỆU THAM KHẢO" in raw_title.upper():
                        is_in_reference_section = True
                        if len(doc.paragraphs) > 0:
                            doc.add_page_break()
                        p = doc.add_paragraph(raw_title)
                        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.paragraph_format.first_line_indent = Cm(0)
                        for run in p.runs:
                            run.font.name = 'Times New Roman'
                            run.font.bold = True
                            run.font.size = Pt(13)
                        continue
                        
                    level = int(element.name[1])
                    # Ngắt trang trước Heading 1 hoặc trước mỗi Phụ lục độc lập
                    is_appendix = "PHỤ LỤC" in raw_title.upper()
                    if (level == 1 or is_appendix) and len(doc.paragraphs) > 0:
                        doc.add_page_break()
                    heading = doc.add_heading(raw_title, level=level)
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
                            li_text = clean_latex_and_text(li.text)
                            for subline in li_text.split('\n'):
                                # Gỡ bỏ ký tự gạch đầu dòng/bullet hoặc số thứ tự ở đầu list item
                                subline = re.sub(r'^\s*[-•]\s*', '', subline)
                                if not is_in_reference_section:
                                    subline = re.sub(r'^\s*\d+[\.\)]\s+', '', subline)
                                raw_lines.append(subline)
                    else:
                        for p_line in clean_latex_and_text(element.text).split('\n'):
                            # Với thẻ đoạn văn thông thường (p), chỉ gỡ bỏ gạch đầu dòng bullet nếu có,
                            # tuyệt đối KHÔNG xóa số đầu câu để tránh làm mất năm (như 2023.) hoặc số liệu.
                            p_line = re.sub(r'^\s*[-•]\s*', '', p_line)
                            raw_lines.append(p_line)

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
                            if is_in_reference_section:
                                # Đánh số thứ tự cho tài liệu tham khảo và thụt lề toàn bộ đoạn
                                p = doc.add_paragraph(f"{ref_counter}. {line}")
                                p.paragraph_format.left_indent = Cm(1.27)
                                p.paragraph_format.first_line_indent = Cm(-1.27)
                                ref_counter += 1
                            else:
                                # Nhận diện tiêu đề Bảng/Hình/Sơ đồ và Nguồn
                                is_caption = bool(re.match(r'^(Bảng|Hình|Sơ đồ)\s+\d+(\.\d+)*[:.]', line, re.IGNORECASE))
                                is_source = bool(re.match(r'^\(?\*?Nguồn[:\s]', line, re.IGNORECASE))
                                
                                p = doc.add_paragraph(line)
                                if is_caption:
                                    p.paragraph_format.first_line_indent = Cm(0)
                                    for run in p.runs:
                                        run.font.bold = True
                                elif is_source:
                                    p.paragraph_format.first_line_indent = Cm(0)
                                    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                                    for run in p.runs:
                                        run.font.italic = True
                                else:
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

    doc.save(output_file)
    print(f"Đã xuất thành công báo cáo chuẩn NEU ra file: {output_file}")

if __name__ == "__main__":
    draft_dir = sys.argv[1] if len(sys.argv) > 1 else "drafts"
    create_neu_standard_doc(draft_dir)
