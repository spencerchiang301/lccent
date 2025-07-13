$(document).ready(function() {
    // 自動隱藏提示訊息
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);
    
    // 更新購物車數量時的即時回饋
    $('.update-cart-form').on('submit', function(e) {
        const form = $(this);
        const quantity = form.find('input[name="quantity"]').val();
        
        if (quantity < 1) {
            e.preventDefault();
            if (confirm('確定要移除此商品嗎？')) {
                form.find('input[name="quantity"]').val(0);
                form.submit();
            }
        }
    });
    
    // 加入購物車的動畫效果
    $('.add-to-cart-form').on('submit', function(e) {
        const button = $(this).find('button[type="submit"]');
        const originalText = button.text();
        
        button.text('加入中...').prop('disabled', true);
        
        setTimeout(function() {
            button.text(originalText).prop('disabled', false);
        }, 1000);
    });
    
    // 數量輸入框限制
    $('input[type="number"]').on('input', function() {
        const max = parseInt($(this).attr('max'));
        const value = parseInt($(this).val());
        
        if (value > max) {
            $(this).val(max);
        } else if (value < 1) {
            $(this).val(1);
        }
    });
});

// 確認刪除功能
function confirmDelete(message) {
    return confirm(message || '確定要刪除嗎？');
}