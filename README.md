# NEU Research Writer (Bộ công cụ & Khung làm việc NCKH Nhóm 19)

> **Đề tài:** Ảnh hưởng của việc sử dụng dịch vụ Mua trước trả sau (BNPL) đến hành vi mua sắm bốc đồng của sinh viên tại Hà Nội: Vai trò điều tiết của hiểu biết tài chính  
> **Đơn vị:** Khoa Khoa học Quản lý - Trường Đại học Kinh tế Quốc dân (NEU)  
> **GVHD:** TS. Phùng Minh Thu Thủy  
> **Nhóm nghiên cứu (Nhóm 19):** Tống Gia Bảo (Trưởng nhóm), Vũ Anh Khôi, Doãn Quỳnh Anh, Võ Thái Lâm, Nguyễn Thái Phương Trinh.

---

## 1. Mục tiêu & Nguyên tắc vận hành

1. **Khóa trí nhớ hệ thống (`templates/project-context.md`):** Đã khóa cứng 100% bối cảnh đề tài, Outline 5 chương, 15 biến quan sát (`BNPL1`–`BNPL4`, `FL1`–`FL6`, `IB1`–`IB5`), 03 biến kiểm soát (`CONTROL1`–`CONTROL3`) và **27 tài liệu tham khảo đã xác thực chuẩn APA 7th**.
2. **Quy chuẩn khoa học tiệm cận Q1:** Áp dụng tư duy lập luận "Vòng lặp học thuật khép kín" kết hợp cơ chế kiểm định chất lượng 2 vòng (Pass 1 - Cốt lõi & Pass 2 - Định dạng) trong `checklists/chapter-qa-gate.md`.
3. **Phân nhánh độc lập cho 5 thành viên:** Mỗi thành viên sở hữu 01 branch riêng biệt để viết các phần được phân công, tránh xung đột mã nguồn (merge conflict) và dễ dàng quản lý tiến độ.
4. **Tự động hóa xuất bản Word chuẩn NEU:** Tự động hợp nhất 39 file bản thảo Markdown trong thư mục `drafts/` thành file báo cáo nghiệm thu hoàn chỉnh [BaoCaoTongKet.docx](file:///d:/neu-research-writer/BaoCaoTongKet.docx) chuẩn lề, font Times New Roman 13pt, bảng viền Table Grid và phân trang tự động.

---

## 2. Cấu trúc thư mục dự án

```text
neu-research-writer/
├── README.md                              # Cẩm nang hướng dẫn sử dụng và quy trình làm việc nhóm
├── SKILL.md                               # Bộ quy tắc điều phối AI lõi (luật khoa học, trích dẫn, định tuyến)
├── BaoCaoTongKet.docx                     # File báo cáo toàn văn tổng hợp xuất ra chuẩn mẫu NEU
├── requirements.txt                       # Danh mục thư viện Python cần thiết
├── drafts/                                # HỆ THỐNG 39 FILE BẢN THẢO OUTLINE 5 CHƯƠNG ĐÃ KHÓA
│   ├── 00-01-Loi-cam-doan.md
│   ├── 00-02-Danh-muc-Bang-bieu.md        # Trình bày dạng Bảng Markdown
│   ├── 00-03-Danh-muc-Hinh.md             # Trình bày dạng Bảng Markdown
│   ├── 00-04-Danh-muc-Tu-viet-tat.md      # Trình bày dạng Bảng Markdown
│   ├── 01-00-Chuong-1-Gioi-thieu.md đến 01-1.6-... (Chương 1: Giới thiệu đề tài)
│   ├── 02-00-Chuong-2-... đến 02-2.4-...          (Chương 2: Cơ sở lý thuyết & Mô hình)
│   ├── 03-00-Chuong-3-... đến 03-3.5-...          (Chương 3: Phương pháp nghiên cứu)
│   ├── 04-00-Chuong-4-... đến 04-4.4-...          (Chương 4: Kết quả nghiên cứu & Thảo luận)
│   ├── 05-00-Chuong-5-... đến 05-5.4-...          (Chương 5: Kết luận & Hàm ý quản trị)
│   ├── 99-00-Tai-lieu-tham-khao.md                # 27 tài liệu tham khảo chuẩn APA 7th
│   ├── 99-01-Phu-luc-1-Phieu-dieu-tra-khao-sat.md # Phụ lục 1
│   ├── 99-02-Phu-luc-2-Thong-ke-mo-ta-mau.md      # Phụ lục 2
│   └── 99-03-Phu-luc-3.md                         # Phụ lục 3: Kết quả phân tích phần mềm
├── scripts/
│   └── export_to_docx.py                  # Script biên dịch tự động drafts/*.md -> BaoCaoTongKet.docx
├── references/                            # 10 Module cẩm nang hướng dẫn phương pháp học thuật chuyên sâu
│   ├── 00-outline-architect.md            # Nguyên tắc cấu trúc outline & phân tầng mục lục
│   ├── 01-intro-and-gap.md                # Viết Mở đầu & Ma trận khoảng trống 4 tầng
│   ├── 02-literature-and-hypotheses.md    # Viết Tổng quan 2 chiều, Lý thuyết nền & Giả thuyết
│   ├── 03-methodology.md                  # Viết Phương pháp, Thiết kế chọn mẫu & Thang đo
│   ├── 04-results-and-discussion.md       # Báo cáo thực nghiệm 4 tầng & Thảo luận đối chiếu
│   ├── 05-implications-and-conclusion.md  # Viết Khuyến nghị neo số liệu & Kết luận
│   ├── 06-literature-matrix-extractor.md  # Trích xuất và lập ma trận tổng quan bài báo mới
│   ├── 07-citations-and-appendices.md     # Chuẩn trích dẫn APA 7th & Quy chuẩn phụ lục
│   ├── 08-merge-and-paraphrase.md         # Hợp nhất liên chương, chuyển ý & khử trùng lặp Turnitin
│   ├── 09-defense-and-viva-prep.md        # Giả lập phản biện hội đồng & câu hỏi bảo vệ
│   └── methods/
│       └── survey-sem-guide.md            # Bộ ngưỡng PLS-SEM (SmartPLS 4) & CB-SEM (SPSS/AMOS)
├── checklists/
│   └── chapter-qa-gate.md                 # Bộ lọc tự kiểm định 2 vòng trước khi bàn giao bản thảo
└── templates/
    ├── project-context.md                 # Xương sống thông tin đề tài (ĐÃ ĐIỀN ĐỦ THÔNG TIN NHÓM 19)
    └── chapter-handoff.md                 # Phiếu bàn giao số liệu thực nghiệm giữa các chương
```

---

## 3. Hệ thống Nhánh (Git Branches) & Phân công nhiệm vụ

Toàn bộ nhóm vận hành trên GitHub repository `tongadam8-max/neu-research-writer` với **nhánh mặc định là `BNPL-gr19`**. Mỗi thành viên làm việc trên nhánh độc lập:

| STT | Thành viên | Nhánh (Branch) | Nhiệm vụ chính được phân công |
| :---: | :--- | :---: | :--- |
| 1 | **Tống Gia Bảo** (Trưởng nhóm) | `bao` | Điều phối chung, duyệt PR, Chương 1 & Phụ lục |
| 2 | **Vũ Anh Khôi** | `khoi` | Chương 2: Cơ sở lý thuyết & Phát triển giả thuyết |
| 3 | **Doãn Quỳnh Anh** | `qanh` | Chương 3: Phương pháp nghiên cứu & Thang đo |
| 4 | **Võ Thái Lâm** | `lam` | Chương 4: Kết quả xử lý SmartPLS 4 / SPSS 27 |
| 5 | **Nguyễn Thái Phương Trinh** | `trinh` | Chương 4 (Thảo luận) & Chương 5: Khuyến nghị, Kết luận |

---

## 4. Hướng dẫn quy trình làm việc cho từng thành viên

### Bước 1: Kéo code và chuyển về nhánh cá nhân
Trước khi bắt đầu viết, mở Terminal (PowerShell / Git Bash) tại thư mục dự án:
```bash
git fetch origin
git checkout <tên_nhánh_của_bạn>
# Ví dụ đối với Khôi: git checkout khoi
git pull origin <tên_nhánh_của_bạn>
```

### Bước 2: Triển khai viết bản thảo cùng AI
Bạn có thể sử dụng AI Agent (Antigravity, Cursor, Windsurf, Claude Code) hoặc bản Web (Gemini / ChatGPT):
- **Nếu dùng AI Agent trong IDE:** Chỉ thị cho AI đọc `templates/project-context.md` và viết trực tiếp vào file tương ứng trong thư mục `drafts/` (ví dụ: `drafts/02-2.1-Cac-khai-niem-co-ban.md`).
- **Nếu dùng Web (ChatGPT / Claude / Gemini):** Đính kèm các file:
  1. `SKILL.md` (Bộ quy tắc bắt buộc)
  2. `templates/project-context.md` (Bối cảnh đề tài, thang đo, 27 trích dẫn)
  3. `references/<module_tương_ứng>.md`
  4. Bảng số liệu hoặc tóm tắt tài liệu của bạn (nếu viết Chương 4 hoặc Chương 2).

### Bước 3: Kiểm tra chất lượng trước khi nộp
Mọi đoạn văn trước khi lưu vào `drafts/` bắt buộc phải vượt qua bộ lọc tại `checklists/chapter-qa-gate.md`:
- [x] Không gạch đầu dòng (-) trong thân bài; viết đoạn văn học thuật hoàn chỉnh dùng từ nối `Thứ nhất, Thứ hai...`.
- [x] Không bịa trích dẫn (chỉ dùng trong 27 nguồn đã xác thực hoặc Hair et al., Cohen).
- [x] Không bọc ngoặc kép vào các thuật ngữ như Mua trước trả sau, Hiểu biết tài chính, Mua sắm bốc đồng.

### Bước 4: Lưu thay đổi và đẩy lên GitHub
Sau khi hoàn thành phần viết của mình:
```bash
git add drafts/
git commit -m "feat(chX): viết hoàn thiện mục X.X theo chuẩn NEU"
git push origin <tên_nhánh_của_bạn>
```

### Bước 5: Hợp nhất vào nhánh chính (`BNPL-gr19`)
Lên giao diện GitHub, tạo một **Pull Request (PR)** từ nhánh của bạn vào nhánh `BNPL-gr19`. Trưởng nhóm (Gia Bảo) sẽ review và hợp nhất nội dung.

---

## 5. Hướng dẫn xuất Báo cáo toàn văn ra Word (`.docx`)

Sau khi các file trong `drafts/` được cập nhật, bất kỳ thành viên nào cũng có thể chạy lệnh để xuất file Word nghiệm thu:

1. **Cài đặt thư viện (chỉ cần chạy lần đầu tiên):**
   ```bash
   pip install -r requirements.txt
   ```
2. **Thực thi script xuất Word:**
   ```bash
   python scripts/export_to_docx.py
   # hoặc nếu dùng môi trường ảo:
   .venv\Scripts\python.exe scripts\export_to_docx.py
   ```
3. File kết quả sẽ được tạo tại [BaoCaoTongKet.docx](file:///d:/neu-research-writer/BaoCaoTongKet.docx) với đầy đủ định dạng chuẩn:
   - Lề chuẩn: Trái 3,5 cm; Phải 2,0 cm; Trên 2,5 cm; Dưới 2,5 cm.
   - Giãn dòng 1.5 lines, thụt đầu dòng 1,27 cm, căn đều 2 bên (Justify).
   - Tự động ngắt trang hợp lý giữa các chương, tài liệu tham khảo và từng phụ lục.

---

## 6. Bộ câu lệnh mẫu (Prompt Templates)

Dưới đây là các câu lệnh mẫu được tối ưu sẵn để bạn sao chép khi làm việc với AI:

### Viết Tổng quan nghiên cứu (Mục 1.1)
> "Áp dụng `SKILL.md`, `references/01-intro-and-gap.md` và Mục 1 của `references/02-literature-and-hypotheses.md` dựa trên `templates/project-context.md`. Hãy viết toàn văn tiểu mục 1.1 Tổng quan nghiên cứu vào file `drafts/01-1.1-Tong-quan-nghien-cuu.md`. Áp dụng phương pháp tổng hợp ma trận 2 chiều, gom nhóm các tác giả cùng quan điểm từ Kho 27 tài liệu xác thực và làm nổi bật các tranh luận học thuật."

### Viết Phát triển Giả thuyết nghiên cứu (Mục 2.3)
> "Áp dụng `SKILL.md` và `references/02-literature-and-hypotheses.md` dựa trên `templates/project-context.md`. Hãy viết toàn văn tiểu mục 2.3 Phát triển giả thuyết nghiên cứu vào file `drafts/02-2.3-Phat-trien-gia-thuyet-nghien-cuu.md`. Triển khai đầy đủ H1 (+), H2 (-) và phân tích sâu cơ chế hai chiều của H3 (H3a kìm hãm theo Thuyết Xử lý kép vs. H3b khuếch đại theo nghịch lý BNPL)."

### Báo cáo Kết quả kiểm định mô hình (Mục 4.2 & 4.3)
> "Áp dụng `SKILL.md`, `references/04-results-and-discussion.md` và `references/methods/survey-sem-guide.md`. Dựa trên bảng số liệu SmartPLS 4 tôi cung cấp dưới đây, hãy lập bảng chuẩn và viết đoạn văn phân tích thực nghiệm thuần túy vào file `drafts/04-4.2-Danh-gia-mo-hinh-do-luong-Outer-Model.md` và `drafts/04-4.3-Danh-gia-mo-hinh-cau-truc-Inner-Model-va-Kiem-dinh-gia-thuyet.md`. Tuyệt đối tuân thủ quy tắc Zero Number Drift và kiểm định hai phía cho biến điều tiết: [Dán kết quả phần mềm]."

### Viết Thảo luận kết quả nghiên cứu (Mục 4.4)
> "Áp dụng `SKILL.md` và `references/04-results-and-discussion.md` (Phần B) dựa trên `templates/project-context.md` và `templates/chapter-handoff.md`. Hãy viết toàn văn tiểu mục 4.4 Thảo luận kết quả nghiên cứu vào file `drafts/04-4.4-Thao-luan-ket-qua-nghien-cuu.md`. Đối chiếu sâu sắc từng phát hiện với Thuyết Kế toán tâm lý, Thuyết Xử lý kép và các công trình thực chứng quốc tế/Việt Nam đã tổng quan."

### Viết Khuyến nghị & Hàm ý quản trị (Mục 5.3)
> "Áp dụng `SKILL.md` và `references/05-implications-and-conclusion.md` dựa trên kết quả ở `templates/chapter-handoff.md`. Hãy viết toàn văn tiểu mục 5.3 Khuyến nghị vào file `drafts/05-5.3-Khuyen-nghi-va-Ham-y-thuc-tien.md`. Áp dụng kỹ thuật Neo số liệu: mở đầu bằng các hệ số thực nghiệm, sau đó đề xuất các giải pháp khả thi theo đúng 3 nhóm chủ thể (Sinh viên; Nhà trường & Đoàn thanh niên; Cơ quan quản lý & Fintech BNPL)."
