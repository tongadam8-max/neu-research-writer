import os
import sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_neu_standard_doc(input_folder, output_file="BaoCaoTongKet.docx"):
    """
    Quét tất cả file .md trong thư mục drafts, ghép lại và xuất ra file Word
    theo chuẩn định dạng NEU: Times New Roman 13, Line spacing 1.5,
    Margins: Top/Bottom 2.5cm, Left 3.5cm, Right 2cm.
    """
    try:
        import markdown
        from bs4 import BeautifulSoup
    except ImportError:
        print("Vui lòng cài đặt: pip install python-docx markdown beautifulsoup4")
        return

    doc = Document()
    
    # Thiết lập margin chuẩn NEU
    sections = doc.sections
    for section in sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.5)
        section.right_margin = Cm(2.0)

    # Thiết lập Font chữ mặc định
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(13)
    
    paragraph_format = style.paragraph_format
    paragraph_format.line_spacing = 1.5
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Ghép file
    if not os.path.exists(input_folder):
        print(f"Không tìm thấy thư mục {input_folder}")
        return

    md_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.md')])
    if not md_files:
        print("Không có file .md nào để xuất.")
        return

    for md_file in md_files:
        with open(os.path.join(input_folder, md_file), 'r', encoding='utf-8') as f:
            md_text = f.read()
            html = markdown.markdown(md_text)
            soup = BeautifulSoup(html, 'html.parser')
            
            for element in soup:
                if element.name in ['h1', 'h2', 'h3']:
                    heading = doc.add_heading(element.text, level=int(element.name[1]))
                    for run in heading.runs:
                        run.font.name = 'Times New Roman'
                        if element.name == 'h1': run.font.size = Pt(16)
                        elif element.name == 'h2': run.font.size = Pt(14)
                        else: run.font.size = Pt(13)
                elif element.name == 'p':
                    doc.add_paragraph(element.text)
                elif element.name == 'ul':
                    for li in element.find_all('li'):
                        doc.add_paragraph(li.text, style='List Bullet')
            doc.add_page_break()

    doc.save(output_file)
    print(f"Đã xuất thành công báo cáo chuẩn NEU ra file: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        draft_dir = sys.argv[1]
    else:
        draft_dir = "drafts"
    create_neu_standard_doc(draft_dir)
