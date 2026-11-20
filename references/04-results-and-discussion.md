# HƯỚNG DẪN VIẾT CHƯƠNG KẾT QUẢ NGHIÊN CỨU & THẢO LUẬN

Áp dụng module này khi viết **Chương Kết quả nghiên cứu** và **Mục Thảo luận kết quả**.

> **Kiểm tra chế độ bố cục trong `project-context.md` trước khi viết:**
> - **Bố cục báo cáo (4 chương hay 5 chương):** Tuân thủ tuyệt đối danh số và tên chương trong Outline tại Mục 3 của `project-context.md` (không gắn cứng số chương mặc định).
> - **Chế độ Tách riêng:** Chương/Mục Kết quả tập trung **báo cáo kết quả thực nghiệm thuần túy** (bảng biểu, kiểm định giả thuyết, đồ thị, diễn giải ngắn gọn ý nghĩa thống kê); phần **Thảo luận đối chiếu nghiên cứu trước** viết sâu ở chương/mục riêng biệt tiếp theo.
> - **Chế độ Gộp chung:** Viết kết quả kiểm định giả thuyết gắn liền ngay với phần thảo luận đối chiếu lý thuyết và nghiên cứu trước trong cùng một chương/tiểu mục.

> **Yêu cầu phối hợp:** Luôn đọc kèm `references/methods/survey-sem-guide.md` để chuẩn hóa bảng biểu và cách đọc chỉ số.

---

## PHẦN A: QUY CHUẨN BÁO CÁO KẾT QUẢ THỰC NGHIỆM

### 1. Luật vàng chống sai lệch dữ liệu (Zero Number Drift)
- Chỉ sử dụng chính xác con số có trong output phần mềm do thành viên cung cấp.
- Trước khi viết lời bình cho bất kỳ bảng nào, tự cộng kiểm tra lại tổng số quan sát ($N$) và tổng tỷ lệ phần trăm ($100\%$).
- Mọi con số nêu trong đoạn văn bắt buộc phải khớp từng chữ số thập phân với bảng ngay cạnh. Thống nhất dùng dấu phẩy `,` cho số thập phân trong văn bản tiếng Việt (ví dụ: `0,752` hoặc `45,6%`), trừ khi bảng xuất gốc yêu cầu giữ dấu chấm `.` (phải thống nhất toàn bài).

### 2. Trình tự báo cáo chuẩn theo 4 tầng

#### Tầng 1: Kết quả làm sạch dữ liệu, Thống kê mô tả mẫu & Thực trạng
- Mở đầu bằng 1 đoạn ngắn báo cáo hành trình dữ liệu: *Tổng số phiếu thu về -> Số phiếu bị loại theo từng lớp lọc (sai sàng lọc, sai câu bẫy chú ý, thiếu dữ liệu) -> Số phiếu hợp lệ cuối cùng ($N$) và tỷ lệ hợp lệ (%).*
- Trình bày Bảng Thống kê mô tả mẫu nhân khẩu học & các biến kiểm soát, kèm Bảng/Biểu đồ thực trạng hành vi sử dụng (nếu có).
- **Kỹ thuật bình luận thông minh:** KHÔNG đọc lại toàn bộ từng dòng của bảng một cách máy móc. Hãy:
  1. Nêu nhóm chiếm tỷ trọng cao nhất và thấp nhất.
  2. Chỉ ra cấu trúc phân bố của mẫu (có phản ánh đúng đặc trưng tổng thể mục tiêu hay không).
  3. Rút ra 2-3 nhận xét nổi bật về thực trạng sử dụng (tần suất, nền tảng chủ đạo, quy mô giao dịch/mức độ đồng tình trung bình).

#### Tầng 2: Kiểm định tiền phân tích & Đánh giá Mô hình đo lường (Outer Model / EFA-CFA)
- Nếu có kiểm định phân phối chuẩn (Skewness/Kurtosis) hoặc kiểm định sai lệch phương pháp chung (Harman's single-factor CMB), báo cáo gọn ngay đầu mục này.
- Báo cáo đầy đủ theo đúng bộ chỉ số của nhánh phần mềm trong `survey-sem-guide.md` (Hệ số tải, Cronbach's Alpha, CR, AVE, Giá trị phân biệt Fornell-Larcker & HTMT).
- **Quy tắc minh bạch tinh lọc thang đo:**
  - Nếu toàn bộ biến đạt ngưỡng: Khẳng định rõ phạm vi dao động (ví dụ: *"Outer Loadings dao động từ 0,721 đến 0,894, đều vượt ngưỡng 0,70"*).
  - Nếu có biến quan sát bị loại do tải thấp hoặc tải chéo: Báo cáo rõ vòng 1 -> biến nào bị loại vì lý do gì -> kết quả vòng 2 sau khi loại.
  - Nếu xảy ra hiện tượng tách nhân tố ngoài dự kiến: Báo cáo minh bạch cấu trúc nhân tố mới và **dùng cơ sở lý thuyết + bối cảnh Việt Nam để biện giải hợp lý**.
- **Nhắc lại tường minh:** Các biến kiểm soát đơn mục không đánh giá ở bước này.

#### Tầng 3: Đánh giá Mô hình cấu trúc (Inner Model / SEM) & Kiểm định giả thuyết trực tiếp
1. **Đánh giá đa cộng tuyến:** Báo cáo bảng giá trị VIF của tất cả các biến độc lập, biến điều tiết/trung gian và **tất cả các biến kiểm soát** so với ngưỡng chuẩn (`VIF < 3,0` hoặc `< 5,0`).
2. **Đánh giá năng lực giải thích & Quy mô tác động:** Báo cáo $R^2$ (và $R^2$ hiệu chỉnh) của biến phụ thuộc, kèm quy mô tác động $f^2$ của từng biến dự báo theo phân loại của Cohen (nhỏ/trung bình/lớn).
3. **Kiểm định giả thuyết bằng Bootstrapping:**
   - Trình bày Bảng Kết quả kiểm định giả thuyết chuẩn (Quan hệ | Hệ số chuẩn hóa $\beta$ | Độ lệch chuẩn $STDEV$ hoặc $S.E.$ | Giá trị $t$ hoặc $C.R.$ | Giá trị $p$ / $Sig.$ | Kết luận).
   - Trình bày rõ kết quả tác động của các **biến kiểm soát** (biến nào có ý nghĩa thống kê, biến nào không có ý nghĩa, cho thấy tác động chính của mô hình giữ vững ngay cả khi kiểm soát nhiễu).
   - So sánh thứ tự mức độ tác động mạnh/yếu giữa các yếu tố có ý nghĩa thống kê dựa trên trị tuyệt đối của hệ số chuẩn hóa $|\beta|$.

#### Tầng 4: Kiểm định cơ chế mở rộng (Điều tiết / Trung gian)
- **Nếu là Kiểm định Điều tiết (Moderation):**
  1. Báo cáo hệ số đường dẫn, $t$-value và $p$-value (two-tailed) của biến tương tác (`X x M -> Y`) và sự thay đổi của $R^2$ hoặc $f^2$ khi thêm biến tương tác.
  2. Khẳng định giả thuyết điều tiết được chấp nhận theo chiều kìm hãm ($\beta < 0$), khuếch đại/nghịch lý ($\beta > 0$), hay không có ý nghĩa thống kê ($p \ge 0,05$).
  3. **Phân tích Đồ thị Simple Slope Plot:** Dẫn chiếu hình vẽ và mô tả cụ thể độ dốc của đường quan hệ `X -> Y` tại 3 mức của biến điều tiết (`-1 SD` Thấp, `Mean` Trung bình, `+1 SD` Cao): Đường nào dốc hơn, đường nào phẳng hơn, điều đó phản ánh sự khác biệt hành vi gì giữa hai nhóm đối tượng?
- **Nếu là Kiểm định Trung gian (Mediation):**
  1. Trình bày bảng tổng hợp 3 cột: *Tác động trực tiếp | Tác động gián tiếp | Tác động tổng hợp* (kèm mức ý nghĩa Bootstrapping).
  2. Phân loại chính xác loại hình trung gian: *Trung gian toàn phần* (trực tiếp không có ý nghĩa, gián tiếp có ý nghĩa), *Trung gian một phần* (cả hai cùng có ý nghĩa), hay *Không có vai trò trung gian*.

---

## PHẦN B: CÔNG THỨC THẢO LUẬN KẾT QUẢ 2 NHÁNH (CHUẨN Q1)

Không lặp lại bảng số liệu ở dạng liệt kê khô khan. Với từng phát hiện cốt lõi (từng giả thuyết `H1`, `H2`, `H3`...), áp dụng đúng 1 trong 2 nhánh công thức sau:

### Nhánh 1: Giả thuyết ĐƯỢC CHẤP NHẬN (Supported)
Triển khai theo trình tự 4 bước trong 1-2 đoạn văn sâu sắc:
1. **Nhắc lại bằng chứng thực nghiệm:** Nêu ngắn gọn chiều tác động và hệ số ($\beta = ..., p = ...$).
2. **Giải thích cơ chế cốt lõi (Why):** Kết nối trực tiếp về **Lý thuyết nền** (ở Chương Lý thuyết / Tổng quan) để lý giải *tại sao* dữ liệu lại vận hành như vậy.
3. **Đối chiếu học thuật:** Chỉ ra kết quả này tương đồng với các nghiên cứu quốc tế và trong nước nào đã tổng quan ở Chương Cơ sở lý thuyết / Tổng quan (chỉ trích dẫn nguồn trong kho xác thực).
4. **Hàm ý bối cảnh địa phương:** Lý giải ý nghĩa thực tế của phát hiện này trên đặc trưng nhóm khách thể và thị trường Việt Nam.

### Nhánh 2: Giả thuyết BỊ BÁC BỎ hoặc NGƯỢC CHIỀU KỲ VỌNG (Rejected / Counter-intuitive)
Tuyệt đối không né tránh hay viết qua loa 1-2 câu. Đây là phần ghi điểm rất mạnh trước hội đồng phản biện nếu xử lý sâu theo 4 bước:
1. **Thừa nhận khách quan:** Nêu rõ kết quả kiểm định ($\beta = ..., p = ...$) cho thấy chưa đủ bằng chứng thống kê (hoặc chiều tác động ngược với giả thuyết ban đầu).
2. **Đối chiếu sự khác biệt:** Chỉ rõ kết quả này khác biệt với dòng nghiên cứu nào (thường ở các nền kinh tế phát triển) và tương đồng với nghiên cứu nghịch lý nào (nếu có).
3. **Hệ thống hóa 2-3 nguyên nhân có chiều sâu:** Đánh số rõ ràng (`Thứ nhất,... Thứ hai,... Thứ ba,...`), phân tích theo các góc độ thực chứng:
   - *Nguyên nhân tâm lý / nhận thức* (ví dụ: khoảng cách từ kiến thức lý thuyết đến thực hành tự kiểm soát, tâm lý tự tin thái quá).
   - *Nguyên nhân bối cảnh / thể chế / hạ tầng* (đặc thù thị trường mới nổi, mức độ hoàn thiện khung pháp lý, thói quen tiêu dùng địa phương).
   - *Nguyên nhân đặc trưng mẫu khảo sát* (độ đồng nhất của nhóm đối tượng, quy mô ngân sách chi tiêu).
4. **Gợi mở nghiên cứu:** Chốt 1 câu chuyển hướng xem đây là khoảng trống thú vị để đào sâu ở phần Hạn chế & Hướng nghiên cứu tiếp theo.
