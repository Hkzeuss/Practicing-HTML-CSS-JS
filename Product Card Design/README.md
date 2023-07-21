# Có Bug và mình cũng chưa fix được
Ở phần source có đoạn mình đã code như sau: (dòng 19->36 theo source của mình)
.card{  
    margin: 120px auto; 
    width: 320px; 
    height: 400px; 
    background: #272D40; 
    padding: 20px; /*Khoảng cách từ nội dung đến viền của phần tử card là 20px */
    border-radius: 15px; 
    color: white; 
    position: relative; 
}

.card_heart, .card_cart{ 
    font-size: 25px; 
    position: absolute; 
    left: 20px; 
    top: 15px; 
    cursor: pointer; 
}

_Mình đã thêm đầy đủ position: relative; ở phần tử cha và position: absolute; ở phần tử con. Sau đó có áp dụng hoạt ảnh bàn tay cursor cho "cardheart" và cả cardcart. Vấn đề ở đây là chỉ có cardcart được áp dụng còn cardheart thì lại không. Khi bạn chạy code và di chuột vào phần icon heart và icon cart sẽ thấy phần khác biệt._

_Còn lại đều ổn và theo đúng ý mình. Bạn này dùng lại code nếu muốn thêm gì thì tự thêm theo ý mình nhé. Và ai fix được bug trên thì có thể inbox với mình qua đường link mình để ở profile mình rồi nhé. Cảm ơn mọi người rất nhiều!_