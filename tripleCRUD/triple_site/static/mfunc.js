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

function export_graph() {
    // Perform an AJAX request to export the RDF graph file
    const csrftoken = getCookie('csrftoken');

    fetch('/export/', {
        method: 'GET',
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
        .then(response => {
            if (response.ok) {
                // If the response is successful, trigger the file download
                return response.blob();
            } else {
                // Handle errors
                console.error('Failed to export RDF graph file');
                throw new Error('Failed to export RDF graph file');
            }
        })
        .then(blob => {
            // Create a temporary URL for the blob
            const url = window.URL.createObjectURL(blob);

            // Create a link element to trigger the download
            const link = document.createElement('a');
            link.href = url;
            link.download = 'rdf_graph_file.ttl';  // Set the filename for the download
            document.body.appendChild(link);

            // Trigger the download
            link.click();

            // Clean up
            window.URL.revokeObjectURL(url);
            document.body.removeChild(link);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function showEditForm(id, subject, predicate, object) {
    document.getElementById('editTripleId').value = id;
    document.getElementById('editSubject').value = subject;
    document.getElementById('editPredicate').value = predicate;
    document.getElementById('editObject').value = object;
    document.getElementById('editFormContainer').style.display = 'block';

    var form = document.getElementById('editForm');
    form.action = '/edit-triple/' + id;
}

function cancelEdit() {
    document.getElementById('editFormContainer').style.display = 'none';
}

// function toggleApproval(itemId) {
//     approvalStatus[itemId] = !approvalStatus[itemId];
//     updateButtonColor(itemId);
//     checkAllApproved();
// }

// function checkAllApproved() {
//     var allApproved = true;
//     for (var key in approvalStatus) {
//         if (!approvalStatus[key]) {
//             allApproved = false;
//             break;
//         }
//     }
//     document.getElementById('exportBtn').disabled = !allApproved;
// }

// function updateButtonColor(itemId) {
//     var button = document.getElementById('approvalBtn' + itemId);
//     if (approvalStatus[itemId]) {
//         button.classList.remove('btn-warning');
//         button.classList.add('btn-success');
//     } else {
//         button.classList.remove('btn-success');
//         button.classList.add('btn-warning');
//     }
// }

// var approvalStatus = {};