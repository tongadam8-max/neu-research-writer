# CHUẨN KỸ THUẬT PHÂN TÍCH ĐỊNH LƯỢNG KHẢO SÁT (PLS-SEM & CB-SEM)

Tài liệu tham chiếu kỹ thuật dùng khi viết **Chương Phương pháp** (`03-methodology.md`) và **Chương Kết quả** (`04-results-and-discussion.md`). Kiểm tra mục `Loại hình & Phương pháp chính` trong `project-context.md` để áp dụng đúng **Nhánh A (PLS-SEM)** hoặc **Nhánh B (CB-SEM)**.

---

## NHÁNH A: PLS-SEM (SmartPLS 4.x + SPSS 27) - Ưu tiên chuẩn mô hình có Điều tiết

### A1. Bộ ngưỡng tiêu chuẩn đánh giá (Để khai báo ở Chương Phương pháp & đối chiếu ở Chương Kết quả)

| Giai đoạn | Chỉ số kỹ thuật | Ngưỡng chấp nhận | Nguồn chuẩn mực |
| :--- | :--- | :--- | :--- |
| **Mô hình đo lường (Outer Model)** *(Chỉ áp dụng cho biến tiềm ẩn phản ánh)* | Hệ số tải ngoài (Outer Loadings) | $\ge 0,70$ (hoặc giữ lại mức $0,40 - 0,70$ nếu xóa không cải thiện CR/AVE) | Hair et al. (2019, 2021) |
| | Độ tin cậy nhất quán nội tại (Cronbach's Alpha) | $\ge 0,70$ | Hair et al. (2019) |
| | Độ tin cậy tổng hợp (Composite Reliability - CR / $\rho_c$, $\rho_a$) | $\ge 0,70$ (lý tưởng $< 0,95$ để tránh dư thừa chỉ báo) | Hair et al. (2019) |
| | Giá trị hội tụ (AVE) | $\ge 0,50$ | Fornell & Larcker (1981) |
| | Giá trị phân biệt - Tiêu chuẩn Fornell-Larcker | $\sqrt{AVE}$ của mỗi biến lớn hơn mọi hệ số tương quan với biến khác | Fornell & Larcker (1981) |
| | Giá trị phân biệt - Chỉ số HTMT | $< 0,85$ (nghiêm ngặt) hoặc $< 0,90$ (chấp nhận được với khái niệm gần nghĩa) | Henseler et al. (2015) |
| **Mô hình cấu trúc (Inner Model)** | Đa cộng tuyến (Inner VIF) *(Bao gồm cả biến kiểm soát)* | $< 3,0$ (lý tưởng) hoặc $< 5,0$ (không có đa cộng tuyến nghiêm trọng) | Hair et al. (2019) |
| | Hệ số xác định ($R^2$) | $0,25$ (yếu); $0,50$ (trung bình); $0,75$ (mạnh) *(tùy đặc thù hành vi xã hội)* | Hair et al. (2019) |
| | Quy mô tác động ($f^2$) | $0,02$ (nhỏ); $0,15$ (trung bình); $0,35$ (lớn) | Cohen (1988) |
| | Kiểm định giả thuyết (Bootstrapping 5.000 mẫu) | Kiểm định 2 phía (two-tailed): $t > 1,96$ và $p < 0,05$ (mức ý nghĩa 5%) | Hair et al. (2021) |
| **Kiểm định Điều tiết** | Biến tương tác (`X x M -> Y`) + Simple Slope Plot | $t > 1,96$, $p < 0,05$ (two-tailed); kiểm tra quy mô $f^2$ của tương tác ($0,005$ nhỏ; $0,01$ TB; $0,025$ lớn theo Kenny) | Hair et al. (2021) |

### A2. Quy tắc bắt buộc đối với Biến kiểm soát đơn mục (Single-Item Controls)
- **Trong Outer Model:** Tuyệt đối KHÔNG liệt kê vào bảng Outer Loadings, Cronbach's Alpha, CR, AVE, Fornell-Larcker hay HTMT (vì biến đơn mục mặc định tải bằng 1,00 và không có ý nghĩa kiểm định nhất quán nội tại).
- **Trong Inner Model:** Bắt buộc báo cáo giá trị **VIF** và kết quả kiểm định đường dẫn ($\beta$, $t$-value, $p$-value) của từng biến kiểm soát trỏ vào biến phụ thuộc để chứng minh các tác động chính vẫn vững khi đã kiểm soát biến nhiễu.

### A3. Mẫu Bảng biểu chuẩn cho PLS-SEM (Copy sang Word giữ nguyên cấu trúc)

**Mẫu Bảng Outer Model:**

| Biến tiềm ẩn | Biến quan sát | Outer Loadings | Cronbach's Alpha | CR ($\rho_c$) | AVE |
| :--- | :--- | :---: | :---: | :---: | :---: |
| [Tên biến (Code)] | `CODE1` | 0,xxx | 0,xxx | 0,xxx | 0,xxx |

*(Nguồn: Kết quả phân tích dữ liệu trên SmartPLS 4.x của nhóm nghiên cứu)*

**Mẫu Bảng Inner Model & Kiểm định giả thuyết:**

| Giả thuyết / Đường dẫn | Hệ số tác động ($\beta$) | Độ lệch chuẩn (STDEV) | Giá trị $t$ | Giá trị $p$ | Hệ số $f^2$ | Kết luận |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `H1: X -> Y` | 0,xxx | 0,xxx | x,xxx | 0,xxx | 0,xxx | Chấp nhận / Bác bỏ |
| `H3: M x X -> Y` | -0,xxx | 0,xxx | x,xxx | 0,xxx | 0,xxx | Chấp nhận / Bác bỏ |
| *Kiểm soát:* `CTRL1 -> Y` | 0,xxx | 0,xxx | x,xxx | 0,xxx | 0,xxx | Có / Không có YNTK |

*(Ghi chú: Kiểm định Bootstrapping 5.000 mẫu lặp, hai phía; YNTK = Ý nghĩa thống kê ở mức 5%)*

### A4. Mẫu câu diễn giải Đồ thị Simple Slope (Cho biến điều tiết)
> *"Đồ thị tương tác Simple Slope (Hình x.x) minh họa mối quan hệ giữa `[Biến X]` và `[Biến Y]` tại ba mức độ của `[Biến M]`: thấp (`-1 SD`), trung bình (`Mean`) và cao (`+1 SD`). Có thể nhận thấy đường biểu diễn ở nhóm có `[Biến M]` ở mức thấp có độ dốc [lớn hơn/nhỏ hơn] rõ rệt so với đường biểu diễn ở nhóm có `[Biến M]` ở mức cao. Điều này khẳng định khi `[Biến M]` gia tăng, tác động thúc đẩy của `[Biến X]` lên `[Biến Y]` có xu hướng [suy yếu đi / khuếch đại mạnh hơn], ủng hộ giả thuyết `[H3a/H3b]`."*

---

## NHÁNH B: CB-SEM (SPSS + AMOS) - Dùng cho các đề tài kiểm định thang đo cổ điển

### B1. Bộ ngưỡng tiêu chuẩn đánh giá
1. **Kiểm định tiền phân tích:**
   - Phân phối chuẩn: $|Skewness| \le 2$ (hoặc $\le 3$), $|Kurtosis| \le 7$.
   - Sai lệch phương pháp chung (CMB - Harman's single-factor): Nhân tố đầu tiên không xoay giải thích $< 50\%$ tổng phương sai.
2. **Đánh giá độ tin cậy Cronbach's Alpha:** $\alpha \ge 0,70$ (tốt) hoặc $\ge 0,60$ (chấp nhận được với nghiên cứu khám phá mới); Tương quan biến tổng (Corrected Item-Total Correlation) $\ge 0,30$.
3. **Phân tích nhân tố khám phá (EFA - phép quay Promax):**
   - $0,5 \le KMO \le 1$; Kiểm định Bartlett có $Sig. < 0,05$.
   - $Eigenvalue > 1$; Tổng phương sai trích (Total Variance Explained) $> 50\%$.
   - Hệ số tải nhân tố (Factor Loading) $\ge 0,50$; không tải chéo (chênh lệch hệ số tải giữa hai nhân tố $\ge 0,30$).
4. **Phân tích nhân tố khẳng định (CFA) & Mô hình cấu trúc (SEM) theo Hu & Bentler (1999):**
   - $CMIN/df \le 3$ (tốt $\le 2$); $CFI \ge 0,90$; $TLI \ge 0,90$; $GFI \ge 0,80$ (tốt $\ge 0,90$); $RMSEA \le 0,06$ (chấp nhận $\le 0,08$); $Pclose > 0,05$.
   - Giá trị hội tụ & phân biệt: $CR \ge 0,70$; $AVE \ge 0,50$; $MSV < AVE$; $\sqrt{AVE} >$ tương quan giữa các cặp biến tiềm ẩn.
5. **Kiểm định Trung gian (Bootstrapping 5.000 mẫu trên AMOS):** Báo cáo riêng Bảng tác động trực tiếp (Direct), gián tiếp (Indirect) và tổng hợp (Total) kèm mức ý nghĩa $p$-value để kết luận trung gian toàn phần hay một phần.

### B2. Quy tắc đối với Biến kiểm soát đơn mục trong CB-SEM (SPSS + AMOS)
- **Trong Cronbach's Alpha & EFA/CFA:** Tuyệt đối KHÔNG đưa các biến kiểm soát đơn mục (như Giới tính, Độ tuổi, Thu nhập đơn mục) vào phân tích độ tin cậy Alpha hay mô hình đo lường EFA/CFA, vì chúng là biến quan sát trực tiếp, không phải biến tiềm ẩn đa chỉ báo (multi-item latent construct).
- **Trong Mô hình cấu trúc SEM (AMOS):** Biến kiểm soát đơn mục được đưa thẳng vào sơ đồ SEM dưới dạng biến quan sát (hình chữ nhật) có đường dẫn hồi quy trực tiếp trỏ vào biến phụ thuộc. Báo cáo hệ số chuẩn hóa ($\beta$), sai số chuẩn ($S.E.$), giá trị $C.R.$ và $p$-value tương ứng để chứng minh tính vững của mô hình chính khi kiểm soát biến gây nhiễu.
