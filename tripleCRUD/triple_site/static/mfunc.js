function getCookie(name) {
    const cookieValue = document.cookie.split(';')
        .map(cookie => cookie.trim())
        .find(cookie => cookie.startsWith(name + '='));

    if (cookieValue) {
        return cookieValue.split('=')[1];
    } else {
        return null;
    }
}


function delete_triple(triple_id) {
    // Perform an AJAX request to delete the item
    const csrftoken = getCookie('csrftoken');

    fetch('/delete/' + triple_id, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({}),
    })
        .then(response => {
            if (response.ok) {
                // Item successfully deleted, you can redirect or update the UI as needed
                // window.location.reload();  // Reload the page for demonstration
                window.location.reload();
            } else {
                // Handle errors
                console.error('Failed to delete item');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function logout() {
    // Perform an AJAX request to delete the item
    const csrftoken = getCookie('csrftoken');

    fetch('/sign-out/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({}),
    })
        .then(response => {
            if (response.ok) {
                // Item successfully deleted, you can redirect or update the UI as needed
                // window.location.reload();  // Reload the page for demonstration
                window.location.reload();
            } else {
                // Handle errors
                console.error('Failed to delete item');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function showEditForm(id, subject, predicate, object, sheet_num) {
    document.getElementById('editTripleId').value = id;
    document.getElementById('editSubject').value = subject;
    document.getElementById('editPredicate').value = predicate;
    document.getElementById('editObject').value = object;
    document.getElementById('editFormContainer').style.display = 'block';

    var form = document.getElementById('editForm');
    form.action = '/edit-triple/' + id +'/' + sheet_num;
}

function cancelEdit() {
    document.getElementById('editFormContainer').style.display = 'none';
}