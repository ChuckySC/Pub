// var api = {
//     apiUrl: document.location.origin,

//     // TODO: Add requireAuth and Authorization header.

//     _getHeader: function() {
//         return {
//             'Content-Type': 'application/json'
//         };
//     },
//     _getPrepareRequest: function(url, method, input_data) {
//         let request_package = {
//             url: this.apiUrl + url,
//             type: method,
//             headers: this._getHeader(),
//             contentType: "application/json; charset=utf-8",
//         };
//         if (method !== 'GET') request_package['data'] = JSON.stringify(input_data);

//         return request_package;
//     },
//     _call: function(url, method, input_data = {}) {
//         const request_package = this._getPrepareRequest(url, method, input_data);
//         return new Promise((resolve, reject) => {
//             $.ajax(request_package)
//                 .done(function(data, statusText, xhr) {
//                     resolve({ data, status: xhr.status });
//                 })
//                 .fail(function(data) {
//                     reject({
//                         data: $.parseJSON(data.responseText),
//                         status: data.status
//                     });
//                 });
//         });
//     },
//     get: function(url) {
//         return this._call(url, 'GET');
//     },
//     post: function(url, input_data) {
//         return this._call(url, 'POST', input_data);
//     },
//     put: function(url, input_data) {
//         return this._call(url, 'PUT', input_data);
//     },
//     delete: function(url, input_data) {
//         return this._call(url, 'DELETE', input_data);
//     },



//     // API Endpoints
//     getSections: function() {
//         return this.get('/api/sections/');
//     }
// }