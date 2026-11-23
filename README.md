# NEU Research Writer Skill (Bộ công cụ viết toàn văn NCKH theo từng chương)

Kho lưu trữ bộ kỹ năng chuẩn hóa quy trình viết toàn văn báo cáo Nghiên cứu khoa học sinh viên (cấp Khoa / cấp Trường) tại Đại học Kinh tế Quốc dân (NEU). Bộ công cụ áp dụng tư duy cấu trúc "Vòng lặp học thuật khép kín" tiệm cận chuẩn bài báo quốc tế Q1, đồng thời tuân thủ chặt chẽ quy chuẩn trình bày và tính thực tiễn trong nước.

## 1. Mục tiêu thiết kế

- **Dùng chung cho mọi đề tài:** Tách biệt hoàn toàn quy chuẩn viết (`SKILL.md` & `references/`) khỏi nội dung đề tài cụ thể (`templates/project-context.md`).
- **Đồng bộ hóa làm việc nhóm:** Giúp nhiều thành viên viết các chương khác nhau song song nhưng khi ghép lại vẫn thống nhất 100% văn phong, ký hiệu biến, giả thuyết và mạch lập luận.
- **Chống bịa nguồn & chống lệch số liệu:** Tự động gắn thẻ đánh dấu chỗ thiếu trích dẫn thay vì bịa tài liệu; bắt buộc khớp tuyệt đối số liệu giữa bảng và văn bản.

## 2. Cấu trúc thư mục

```text
neu-research-writer/
├── README.md                              # Tài liệu hướng dẫn này
├── SKILL.md                               # File điều phối lõi (luật văn phong, chống bịa nguồn, định tuyến)
├── drafts/                                # Thư mục chứa các file bản thảo .md để xuất Word
│   └── .gitkeep
├── scripts/
│   └── export_to_docx.py                  # Script Python tự động ghép và xuất bản thảo ra .docx chuẩn NEU
├── references/
│   ├── 00-outline-architect.md            # Kiến trúc sư dựng Outline báo cáo toàn văn (4 hoặc 5 chương)
│   ├── 01-intro-and-gap.md                # Viết Phần Mở đầu & Ma trận khoảng trống 4 tầng
│   ├── 02-literature-and-hypotheses.md    # Viết Tổng quan 2 chiều, Lý thuyết nền & Giả thuyết
│   ├── 03-methodology.md                  # Viết Phương pháp, Thang đo, Pilot & Làm sạch dữ liệu
│   ├── 04-results-and-discussion.md       # Viết Kết quả thực nghiệm & Thảo luận 2 nhánh
│   ├── 05-implications-and-conclusion.md  # Viết Khuyến nghị neo số liệu, Hạn chế & Kết luận
│   ├── 06-literature-matrix-extractor.md  # Trích xuất và lập ma trận tổng quan bài báo mới
│   ├── 07-citations-and-appendices.md     # Chuẩn hóa trích dẫn APA 7th & hệ thống Phụ lục NEU
│   ├── 08-merge-and-paraphrase.md         # Hợp nhất liên chương, chuyển ý & khử trùng lặp Turnitin
│   ├── 09-defense-and-viva-prep.md        # Giả lập phản biện hội đồng & ôn luyện bảo vệ
│   └── methods/
│       └── survey-sem-guide.md            # Bộ ngưỡng thống kê & mẫu bảng PLS-SEM / CB-SEM
├── checklists/
│   └── chapter-qa-gate.md                 # Bộ lọc tự kiểm định 2 vòng (Pass 1 & Pass 2)
└── templates/
    ├── project-context.md                 # File cấu hình dùng chung của nhóm (điền 1 lần/đề tài)
    └── chapter-handoff.md                 # Phiếu bàn giao kết quả giữa các thành viên viết chương
```

## 3. Hướng dẫn cài đặt và sử dụng

### Cách 1: Dành cho thành viên dùng AI Agent (Antigravity / Claude Code / Cursor / Windsurf / Gemini CLI)

1. Clone repo về máy:
   ```bash
   git clone <url-repo-cua-nhom>
   ```
2. Nhóm trưởng điền thông tin khoa học lõi của đề tài cùng **Outline mới của bài báo cáo toàn văn** vào `templates/project-context.md` và commit lên nhánh chính (`main`).
3. Từng thành viên pull code mới nhất về, mở AI Agent tại thư mục repo và gọi trực tiếp theo mục mình phụ trách.

### Cách 2: Dành cho thành viên dùng bản Web (Gemini Web / ChatGPT)

1. Tạo một Project / Gem (hoặc đoạn chat mới cho từng chương).
2. Tải lên (hoặc dán) đúng **3-4 file cần thiết** cho phiên làm việc:
   - `SKILL.md` (luôn đính kèm)
   - `templates/project-context.md` (luôn đính kèm)
   - `references/<file-cua-chuong-dang-viet>.md` (+ `survey-sem-guide.md` nếu viết Phương pháp hoặc Kết quả)
   - `templates/chapter-handoff.md` (bắt buộc khi viết Chương Kết quả, Thảo luận, Khuyến nghị, Kết luận)
3. Dán bảng số liệu hoặc ghi chú tài liệu của bạn kèm câu lệnh mẫu bên dưới.

## 4. Quy trình phối hợp nhóm chuẩn (5 bước)

1. **Khóa khung chung:** Nhóm trưởng tổng hợp thông tin khoa học lõi của đề tài (biến số, thang đo, giả thuyết, kho tài liệu tham khảo) và điền **Outline mới của bài báo cáo hoàn chỉnh** vào `templates/project-context.md` (không lấy lại mục lục của bản thuyết minh đề cương), sau đó commit lên nhánh `main` để cả nhóm dùng chung.
2. **Viết cuốn chiếu từng tiểu mục:** Không ra lệnh "viết cả chương 20 trang trong 1 lượt". Hãy viết từng mục lớn (ví dụ `1.1`, rồi `1.2`, rồi `1.3`) để AI giữ được độ sâu lập luận và chiều dài toàn văn.
3. **Cập nhật phiếu bàn giao:** Sau khi chạy xong dữ liệu và chốt Chương Kết quả, người phụ trách dữ liệu điền toàn bộ hệ số thực tế vào `templates/chapter-handoff.md` và đẩy lên GitHub.
4. **Viết Thảo luận & Khuyến nghị neo số liệu:** Thành viên viết Chương Thảo luận/Khuyến nghị tải `chapter-handoff.md` để AI lập luận bám sát đúng các giả thuyết được chấp nhận/bác bỏ.
5. **Tổng biên tập rà soát:** Trước khi ghép vào file Word nộp Khoa, chạy rà soát từng chương qua `checklists/chapter-qa-gate.md`.

## 5. Bộ câu lệnh mẫu (Prompt Templates)

> *Lưu ý: Tên chương và số thứ tự mục (`x.x`) tự động bám sát theo Outline đã khai báo trong `project-context.md` (hỗ trợ hoàn hảo cả bố cục 4 chương lẫn 5 chương).*

- **Viết Phần Mở đầu / Chương 1 (Giới thiệu):**
  > "Áp dụng `SKILL.md` và `references/01-intro-and-gap.md` dựa trên `project-context.md`. Hãy viết toàn văn Phần Mở đầu / Chương Giới thiệu theo đúng Outline của đề tài và chuẩn văn phong học thuật NEU, triển khai sâu lập luận thực tiễn và khoảng trống lý luận."

- **Viết từng mục Chương Tổng quan & Lý thuyết:**
  > "Áp dụng `SKILL.md` và `references/02-literature-and-hypotheses.md` dựa trên `project-context.md`. Hãy viết toàn văn Mục [Điền mã mục, ví dụ: 1.1 hoặc 2.1 - Tổng quan nghiên cứu] chỉ sử dụng các nguồn trong Kho tài liệu tham khảo đã xác thực và các tóm tắt bài báo sau đây: [Dán ghi chú bài báo]."

- **Viết Chương Phương pháp nghiên cứu:**
  > "Áp dụng `SKILL.md`, `references/03-methodology.md` và `references/methods/survey-sem-guide.md`. Hãy viết toàn văn Mục [Điền mã mục, ví dụ: 2.4 hoặc 3.4 - Phương pháp xử lý dữ liệu], đảm bảo khóa đủ các ngưỡng kiểm định cho mô hình đo lường và cấu trúc, đồng thời nêu rõ quy tắc xử lý biến kiểm soát đơn mục."

- **Viết Chương Kết quả nghiên cứu từ số liệu phần mềm:**
  > "Áp dụng `SKILL.md`, `references/04-results-and-discussion.md` (chế độ Tách riêng Kết quả thuần túy) và `references/methods/survey-sem-guide.md`. Dựa trên bảng xuất SmartPLS/SPSS dưới đây, hãy chuẩn hóa bảng biểu và viết toàn văn Mục [Điền mã mục, ví dụ: 3.2 & 3.3 hoặc 4.2 & 4.3]. Tuyệt đối chỉ dùng số liệu tôi cung cấp: [Dán bảng số liệu]."

- **Viết Chương Thảo luận & Khuyến nghị / Hàm ý quản trị:**
  > "Áp dụng `SKILL.md`, `references/04-results-and-discussion.md` và `references/05-implications-and-conclusion.md` dựa trên `project-context.md` và `chapter-handoff.md`. Hãy viết toàn văn Mục [Điền mã mục, ví dụ: 4.1 & 4.2 hoặc 4.4 & 5.3] (Thảo luận đối chiếu nghiên cứu trước và Hệ thống khuyến nghị neo số liệu cho các chủ thể đã chốt)."


## 6. Nguyên tắc linh hoạt khi có dữ liệu thật & ý tưởng mới (Cơ chế 2 tầng)

Bộ Skill này được thiết kế như một **tài liệu sống (living workflow)** đồng hành cùng nhóm từ lúc bắt đầu viết đến khi có kết quả chạy mô hình thực tế:

- **Tầng 1 - Chuẩn khoa học bắt buộc (Luôn giữ vững):** Không bịa trích dẫn hay số liệu; số liệu trong văn bản khớp 100% với bảng phần mềm; trung thực với biến bị loại hoặc giả thuyết bị bác bỏ; tuân thủ chuẩn phương pháp (PLS-SEM/CB-SEM, luật biến kiểm soát đơn mục), văn phong học thuật NEU và APA 7th.
- **Tầng 2 - Mở hoàn toàn cho dữ liệu mới & cách viết hay hơn:**
  - Thành viên hoàn toàn tự do nạp thêm **bài báo mới, lập luận mới, kiểm định bổ sung** hoặc đề xuất **cách triển khai đoạn văn mượt hơn** so với gợi ý mặc định trong `references/`.
  - Khi chạy mô hình ra **con số thực tế khác với dự kiến đề cương**, dữ liệu thật luôn có quyền ưu tiên cao nhất. AI sẽ phân tích theo số liệu mới và tự động tạo mục **Sync Alert** ở cuối câu trả lời để thành viên cập nhật nhanh vào `project-context.md` / `chapter-handoff.md` cho cả nhóm đồng bộ.


## 7. Cơ chế Tự kiểm định 2 vòng & Phản biện trọng tâm (Bản v1.2)

Để đảm bảo bản thảo đạt độ chỉn chu cao nhất cho bài nghiên cứu học thuật mà không làm chậm tiến độ của thành viên:

- **Tự kiểm định 2 vòng độc lập (2-Pass Self-Audit):** Trước khi xuất bản thảo cuối cùng, AI tự động chạy qua 2 vòng lọc riêng biệt trong `checklists/chapter-qa-gate.md`:
  1. *Vòng 1 (Cốt lõi khoa học & Dữ liệu):* Khớp tuyệt đối số liệu bảng - văn bản, nguồn trích dẫn, luật phương pháp và độ chặt của lập luận.
  2. *Vòng 2 (Trình bày & Độ tự nhiên học thuật):* Soát đánh số Bảng/Hình, chuẩn APA 7th, dấu thập phân, chuyển ý giữa các đoạn và gọt sạch câu từ kiểu "văn AI" sáo rỗng.
- **Hỏi chốt thông minh trước khi viết:** AI chỉ dừng lại hỏi tối đa **2-3 câu ngắn gọn** kèm gợi ý phương án khi yêu cầu thực sự thiếu dữ liệu cốt lõi, mơ hồ hoặc có nguy cơ lệch trọng tâm đề tài. Nếu đầu vào đã rõ, AI tiến hành viết ngay.
- **Phản biện trọng tâm khách quan sau khi viết:** Cuối mỗi bản thảo, mục *Phản biện trọng tâm* sẽ gợi mở các khía cạnh chưa được khai thác hết chiều sâu lý thuyết/thực nghiệm. Nếu nội dung của thành viên đã chặt chẽ, AI ghi nhận đúng thực tế và tuyệt đối không tự bịa thêm lỗi góp ý.