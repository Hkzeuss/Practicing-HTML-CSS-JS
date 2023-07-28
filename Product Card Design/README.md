# 🔥 Mô tả Source 🔥
Đây là 1 sản phẩm code nhỏ về 1 nhánh của kinh doanh. Khi chạy code sẽ ra 1 thẻ sản phẩm có các thuộc tính sau:
* Icon tym sản phẩm
* Icon giỏ thanh toán
* Ảnh minh họa sản phẩm
* ên sản phẩm
* Đơn giá của sản phẩm đó
* Các size của sản phẩm
* Màu sắc của sản phẩm
* Nút: mua và Nút: thêm vào giỏ hàng
  
Thêm các hiệu ứng hình ảnh trượt lên xuống nhìn trông nó đẹp hơn    


# 🔥 Có Bug và mình cũng chưa fix được 🔥
Ở phần source có đoạn mình đã code như sau: (dòng 19->36 theo source của mình):
- .card{  
   -    margin: 120px auto; 
   *    width: 320px; 
   *    height: 400px; 
   *    background: #272D40; 
   *    padding: 20px; 
   *    border-radius: 15px; 
   *    color: white; 
   *    position: relative; 
- }

- .card_heart, .card_cart{ 
   *    font-size: 25px; 
   *    position: absolute; 
   *    left: 20px; 
   *   top: 15px; 
   *   cursor: pointer; 
- }

_Mình đã thêm đầy đủ position: relative; ở phần tử cha và position: absolute; ở phần tử con. Sau đó có áp dụng hoạt ảnh bàn tay cursor cho "cardheart" và cả cardcart. Vấn đề ở đây là chỉ có cardcart được áp dụng còn cardheart thì lại không. Khi bạn chạy code và di chuột vào phần icon heart và icon cart sẽ thấy phần khác biệt._

_Còn lại đều ổn và theo đúng ý mình. Bạn này dùng lại code nếu muốn thêm gì thì tự thêm theo ý mình nhé. Và ai fix được bug trên thì có thể inbox với mình qua đường link mình để ở profile mình rồi nhé. Cảm ơn mọi người rất nhiều!_


# 🔥 Demo 🔥
<div style="display: flex;">
  <img src="https://github.com/Hkzeuss/Practicing-HTML-CSS-JS/blob/main/Product%20Card%20Design/Demo02.jpg" alt="Demo01" style="flex: 50%; padding: 5px; width: 100%;">
  <img src="https://github.com/Hkzeuss/Practicing-HTML-CSS-JS/blob/main/Product%20Card%20Design/Demo02.jpg" alt="Demo02" style="flex: 50%; padding: 5px; width: 100%;">
</div>
