document.addEventListener('DOMContentLoaded', function() {
    const rows = document.querySelectorAll('tbody tr');
    
    rows.forEach(row => {
        const editBtn = row.querySelector('.edit-btn');
        const updateBtn = row.querySelector('.update-btn');
        const spans = row.querySelectorAll('.editable-text');
        const inputs = row.querySelectorAll('.edit-input');
        
        editBtn.addEventListener('click', function() {
            spans.forEach(span => span.style.display = 'none');
            inputs.forEach(input => input.style.display = 'inline-block');
            editBtn.style.display = 'none';
            updateBtn.style.display = 'inline-block';
        });
    });
});
