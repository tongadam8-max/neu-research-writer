import os
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Thiết lập khoảng đệm (padding) chuẩn cho ô trong bảng Word."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for margin_name, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{margin_name}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_formatted_paragraph(doc, element, style='Normal', is_list_item=False):
    """Thêm đoạn văn bản giữ nguyên in đậm (strong/b) và in nghiêng (em/i)."""
    p = doc.add_paragraph(style=style)
    p.paragraph_format.line_spacing = 1.5
    if not is_list_item:
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    for child in element.children:
        if hasattr(child, 'name') and child.name:
            if child.name in ['strong', 'b']:
                run = p.add_run(child.get_text())
                run.font.name = 'Times New Roman'
                run.font.size = Pt(13)
                run.font.bold = True
                run.font.color.rgb = RGBColor(0, 0, 0)
            elif child.name in ['em', 'i']:
                run = p.add_run(child.get_text())
                run.font.name = 'Times New Roman'
                run.font.size = Pt(13)
                run.font.italic = True
                run.font.color.rgb = RGBColor(0, 0, 0)
            elif child.name == 'code':
                run = p.add_run(child.get_text())
                run.font.name = 'Courier New'
                run.font.size = Pt(11)
            else:
                run = p.add_run(child.get_text())
                run.font.name = 'Times New Roman'
                run.font.size = Pt(13)
                run.font.color.rgb = RGBColor(0, 0, 0)
        else:
            text = str(child)
            run = p.add_run(text)
            run.font.name = 'Times New Roman'
            run.font.size = Pt(13)
            run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def create_neu_standard_doc(input_folder="drafts", output_file="BaoCaoTongKet.docx"):
    """
    Quét tất cả file .md trong thư mục input_folder, ghép lại và xuất ra file Word (.docx)
    theo chuẩn định dạng NEU: Times New Roman 13pt, Giãn dòng 1.5 lines,
    Căn lề: Trên 2.5cm, Dưới 2.5cm, Trái 3.5cm, Phải 2.0cm, đầy đủ bảng biểu và danh sách.
    """
    try:
        import markdown
        from bs4 import BeautifulSoup
    except ImportError:
        print("Vui lòng cài đặt thư viện hỗ trợ: pip install python-docx markdown beautifulsoup4")
        return

    if not os.path.exists(input_folder):
        os.makedirs(input_folder, exist_ok=True)
        print(f"Đã tự động khởi tạo thư mục '{input_folder}'. Hãy đặt các file .md bản thảo vào đây.")
        return

    doc = Document()
    
    # Thiết lập căn lề chuẩn NEU cho tất cả sections
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.5)
        section.right_margin = Cm(2.0)

    # Thiết lập Font chữ mặc định Normal
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(13)
    font.color.rgb = RGBColor(0, 0, 0)
    
    paragraph_format = style.paragraph_format
    paragraph_format.line_spacing = 1.5
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    md_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.md')])
    if not md_files:
        print(f"Không tìm thấy file .md nào trong thư mục '{input_folder}'. Hãy đặt các file chương/tiểu mục vào đây.")
        return

    for idx, md_file in enumerate(md_files):
        file_path = os.path.join(input_folder, md_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # Bật extensions tables và fenced_code để phân tích bảng biểu Markdown
        html = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
        soup = BeautifulSoup(html, 'html.parser')
        
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'table', 'blockquote']):
            # Tiêu đề các cấp
            if element.name in ['h1', 'h2', 'h3', 'h4']:
                level = int(element.name[1])
                h = doc.add_heading(element.get_text(), level=level)
                h.paragraph_format.line_spacing = 1.5
                for r in h.runs:
                    r.font.name = 'Times New Roman'
                    r.font.color.rgb = RGBColor(0, 0, 0)
                    r.font.bold = True
                    if level == 1:
                        r.font.size = Pt(16)
                    elif level == 2:
                        r.font.size = Pt(14)
                    else:
                        r.font.size = Pt(13)

            # Đoạn văn bản thông thường (hỗ trợ in đậm, in nghiêng)
            elif element.name == 'p':
                add_formatted_paragraph(doc, element, style='Normal')

            # Danh sách không thứ tự (Bullet points)
            elif element.name == 'ul':
                for li in element.find_all('li', recursive=False):
                    add_formatted_paragraph(doc, li, style='List Bullet', is_list_item=True)

            # Danh sách có thứ tự (Numbered list 1., 2., 3.)
            elif element.name == 'ol':
                for li in element.find_all('li', recursive=False):
                    add_formatted_paragraph(doc, li, style='List Number', is_list_item=True)

            # Khối trích dẫn (Blockquote)
            elif element.name == 'blockquote':
                for p_child in element.find_all('p'):
                    p = add_formatted_paragraph(doc, p_child, style='Normal')
                    p.paragraph_format.left_indent = Cm(1.0)
                    for r in p.runs:
                        r.font.italic = True

            # BẢNG BIỂU HỌC THUẬT (TABLES)
            elif element.name == 'table':
                rows = element.find_all('tr')
                if rows:
                    cols_count = max(len(row.find_all(['th', 'td'])) for row in rows)
                    table = doc.add_table(rows=len(rows), cols=cols_count)
                    table.style = 'Table Grid'
                    
                    for r_idx, row in enumerate(rows):
                        cells = row.find_all(['th', 'td'])
                        for c_idx, cell in enumerate(cells):
                            doc_cell = table.cell(r_idx, c_idx)
                            doc_cell.text = cell.get_text().strip()
                            set_cell_margins(doc_cell, top=80, bottom=80, left=120, right=120)
                            for p in doc_cell.paragraphs:
                                p.paragraph_format.line_spacing = 1.0
                                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if (r_idx == 0 or cell.name == 'th') else WD_ALIGN_PARAGRAPH.LEFT
                                for r in p.runs:
                                    r.font.name = 'Times New Roman'
                                    r.font.size = Pt(11)
                                    if cell.name == 'th' or r_idx == 0:
                                        r.font.bold = True
                    # Thêm khoảng đệm nhỏ sau bảng
                    doc.add_paragraph()

        # Ngắt trang giữa các file chương (ngoại trừ file cuối cùng)
        if idx < len(md_files) - 1:
            doc.add_page_break()

    doc.save(output_file)
    print(f"Đã xuất thành công báo cáo toàn văn chuẩn NEU (có bảng biểu & danh sách) ra file: {output_file}")

if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "drafts"
    create_neu_standard_doc(folder)
