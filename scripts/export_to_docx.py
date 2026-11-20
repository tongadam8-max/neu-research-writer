import os
import sys
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from bs4 import BeautifulSoup
import markdown

def clean_latex_and_text(text):
    """Xóa mã LaTeX thô và chuyển thành ký hiệu Unicode học thuật chuẩn"""
    mapping = {
        r'$\beta$': 'β', r'$p$': 'p', r'$t$': 't', r'$R^2$': 'R²', r'$f^2$': 'f²',
        r'$\alpha$': 'α', r'$\rho$': 'ρ', r'$\rightarrow$': '→', r'$\times$': 'x',
        r'$N$': 'N', r'$100\%$': '100%', r'$\le$': '≤', r'$\ge$': '≥',
        r'\beta': 'β', r'\rightarrow': '→', r'\times': 'x', r'\alpha': 'α'
    }
    for k, v in mapping.items():
        text = text.replace(k, v)
    # Xóa các dấu $ còn sót lại của thẻ math
    text = text.replace('$', '')
    return text.strip()

def create_neu_standard_doc(input_folder, output_file="BaoCaoTongKet.docx"):
    doc = Document()
    
    # 1. Cấu hình Margins chuẩn (Trái 3.5cm, Phải/Trên/Dưới 2cm-2.5cm)
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.5)
        section.right_margin = Cm(2.0)

    # 2. Cấu hình Font và Spacing mặc định
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(13)
    style.paragraph_format.line_spacing = 1.5
    style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    if not os.path.exists(input_folder):
        print(f"Không tìm thấy thư mục {input_folder}")
        return

    md_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.md') and not f.startswith('test-')])
    
    for md_file in md_files:
        with open(os.path.join(input_folder, md_file), 'r', encoding='utf-8') as f:
            html = markdown.markdown(f.read(), extensions=['tables'])
            soup = BeautifulSoup(html, 'html.parser')
            
            for element in soup:
                if element.name in ['h1', 'h2', 'h3', 'h4']:
                    level = int(element.name[1])
                    heading = doc.add_heading(clean_latex_and_text(element.text), level=level)
                    for run in heading.runs:
                        run.font.name = 'Times New Roman'
                        run.font.color.rgb = RGBColor(0, 0, 0) # Khóa màu đen, không dùng màu xanh mặc định
                        if level == 1: run.font.size = Pt(16)
                        elif level == 2: run.font.size = Pt(14)
                        else: run.font.size = Pt(13)
                
                elif element.name == 'p':
                    doc.add_paragraph(clean_latex_and_text(element.text))
                
                elif element.name == 'ul':
                    # Đổi dấu chấm khổng lồ thành gạch ngang chuẩn văn bản hành chính/khoa học Việt Nam
                    for li in element.find_all('li'):
                        p = doc.add_paragraph(f"- {clean_latex_and_text(li.text)}")
                        p.paragraph_format.left_indent = Cm(1.27)
                        p.paragraph_format.first_line_indent = Cm(-0.63)
                
                elif element.name == 'ol':
                    for i, li in enumerate(element.find_all('li'), 1):
                        p = doc.add_paragraph(f"{i}. {clean_latex_and_text(li.text)}")
                        p.paragraph_format.left_indent = Cm(1.27)
                        p.paragraph_format.first_line_indent = Cm(-0.63)
                
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
                            # In đậm Header bảng
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
