# BỘ LỌC TỰ KIỂM ĐỊNH 2 VÒNG TRƯỚC KHI XUẤT BẢN THẢO (2-PASS QA GATE)

Trước khi trả bản thảo cho thành viên (hoặc chốt chỉnh sửa trên file `.md`), AI bắt buộc chạy tuần tự **2 vòng kiểm định độc lập** dưới đây và tự sửa trực tiếp mọi lỗi phát hiện được. **Lưu ý:** Bộ lọc này chỉ bảo vệ chuẩn mực khoa học và chất lượng trình bày; tuyệt đối không dùng để bác bỏ số liệu thực tế mới, nguồn tài liệu mới hay lối viết học thuật sắc bén hơn của tác giả.

---

## VÒNG 1: KIỂM ĐỊNH CỐT LÕI KHOA HỌC, LOGIC & DỮ LIỆU (SUBSTANCE & RIGOR PASS)

- [ ] **1. Khớp thuật ngữ & Ký hiệu hiện hành:** Tên biến, mã biến quan sát và ký hiệu viết tắt khớp với `templates/project-context.md` hoặc bản cập nhật mới nhất do thành viên cung cấp trong phiên làm việc.
- [ ] **2. Zero Number Drift (Khớp số liệu tuyệt đối):** Mọi con số (cỡ mẫu $N$, tần số, tỷ lệ %, hệ số $\beta$, $t$, $p$, VIF, $R^2$, $f^2$, Alpha, CR, AVE, HTMT) trong đoạn văn khớp 100% với bảng số liệu thực tế ngay cạnh. Đã tự cộng kiểm tra tổng $N$ và tổng tỷ lệ thành phần bằng đúng $100\%$.
- [ ] **3. Chống bịa tài liệu & Mở rộng nguồn minh bạch:** 100% trích dẫn trong bài đến từ Kho 27 tài liệu xác thực (`templates/project-context.md`) hoặc các chuẩn mực phương pháp luận quốc tế từ `survey-sem-guide.md` (như Hair et al., Cohen). **Việc bổ sung thêm nguồn trích dẫn mới là hoàn toàn được phép nhưng bắt buộc phải được Trưởng nhóm duyệt HOẶC thành viên khi viết đã tự kiểm tra, đối chiếu kỹ lưỡng nguồn mới** (tác giả, năm, tên bài báo, tạp chí, kết quả thực nghiệm) trước khi đưa vào bài. Tuyệt đối không để AI tự bịa nguồn; mọi luận điểm chưa đủ căn cứ đều được gắn thẻ `[CẦN BỔ SUNG TRÍCH DẪN: ...]`.
- [ ] **4. Trung thực phương pháp & Luật Biến kiểm soát đơn mục:** Không đưa biến kiểm soát đơn mục vào kiểm định thang đo phản ánh, nhưng đã báo cáo đầy đủ VIF và tác động trong Inner Model; công bố minh bạch mọi biến bị loại, nhân tố tách mới hoặc giả thuyết bị bác bỏ.
- [ ] **5. Mạch lập luận & Trọng tâm nghiên cứu:** Các nhận định bám sát lý thuyết nền và câu hỏi nghiên cứu; không suy diễn vượt quá dữ liệu; mọi khuyến nghị đều neo trực tiếp vào kết quả thực nghiệm (nếu có điểm hổng trọng tâm thực sự, ghi ngắn gọn vào mục *Phản biện trọng tâm* cuối bài; không tự nghĩ ra lỗi giả).
- [ ] **6. Đồng bộ liên chương (Sync Alert):** Đã đối chiếu khớp với `templates/chapter-handoff.md` (nếu là chương sau) và ghi nhận mọi thay đổi mới phát sinh vào mục *Ghi chú bàn giao & Đồng bộ*.

---

## VÒNG 2: KIỂM ĐỊNH TRÌNH BÀY, ĐỊNH DẠNG & ĐỘ TỰ NHIÊN HỌC THUẬT (PRESENTATION & POLISH PASS)

- [ ] **7. Độ sâu đoạn văn toàn văn (Anti-Outline):** Không viết kiểu gạch đầu dòng tóm tắt như đề cương hay slide; mỗi luận điểm được triển khai thành đoạn văn học thuật trọn vẹn, có câu chủ đề, lập luận và câu chuyển ý mượt giữa các đoạn/tiểu mục.
- [ ] **8. Văn phong NEU & Loại bỏ "văn AI" sáo rỗng:** Dùng nhất quán ngôi thứ ba (*nhóm tác giả / nhóm nghiên cứu / nghiên cứu này*), sắc thái khách quan; đã gọt sạch các cụm mở đầu lặp cấu trúc hoặc sáo rỗng (*"Trong bối cảnh hiện nay..."*, *"Điều này cho thấy tầm quan trọng to lớn..."*, tính từ cảm tính); không nhầm lẫn giải nghĩa thuật ngữ tiếng Anh/tiếng Việt.
- [ ] **9. Chuẩn định dạng Bảng, Hình & Số thập phân:**
  - Bảng đánh số liên tục `Bảng [Số chương].[Số thứ tự]` (tiêu đề nằm **trên** bảng, nguồn nằm **dưới** bảng).
  - Hình đánh số liên tục `Hình [Số chương].[Số thứ tự]` (tiêu đề và nguồn nằm **dưới** hình).
  - Dẫn chiếu đúng số bảng/hình trong thân bài (không lệch thứ tự) và thống nhất quy tắc dấu thập phân (`,` hoặc `.`) xuyên suốt chương.
- [ ] **10. Chuẩn trích dẫn APA 7th trong văn bản:**
  - 1 tác giả: `(Thaler, 1999)` hoặc `Thaler (1999)`
  - 2 tác giả: `(Lusardi & Mitchell, 2014)` hoặc `Lusardi và Mitchell (2014)`
  - 3 tác giả trở lên: `(Ashby et al., 2025)` hoặc `Ashby và cộng sự (2025)` (thống nhất duy nhất một dạng xuyên suốt cả bài).
- [ ] **11. Cấm tuyệt đối gạch đầu dòng & Đồ thị ASCII:** Cấm sử dụng dấu gạch đầu dòng (-) hoặc chấm tròn (•) để liệt kê ý trong thân bài. Mọi ý phải viết thành đoạn văn hoàn chỉnh, thụt đầu dòng, dùng từ nối 'Thứ nhất, Thứ hai...'. Riêng Danh mục từ viết tắt, Danh mục bảng biểu và Danh mục hình phải trình bày dưới dạng Bảng Markdown (Table Grid). Cấm vẽ đồ thị bằng chữ (ASCII Art), chỉ ghi `[CHÈN HÌNH ẢNH ĐỒ THỊ TỪ PHẦN MỀM VÀO ĐÂY]`.
- [ ] **12. Cấm lạm dụng ngoặc kép/ngoặc đơn:** Tuyệt đối không dùng dấu ngoặc kép ("...", “...”) hoặc ngoặc đơn ('...') để bọc các thuật ngữ chuyên ngành (như Mua trước trả sau, Hiểu biết tài chính, Mua sắm bốc đồng) hoặc bọc các cụm từ ẩn dụ/nhấn mạnh (như không ma sát, chiếc phanh, nỗi đau thanh toán). Viết các cụm từ này như văn bản bình thường. Chỉ dùng ngoặc kép khi trích dẫn đúng nguyên văn một câu nói dài hoặc tên tài liệu.
