new Vue({
    el: '#id_tests',
    data: {
    tests: []
    },
    created: function () {
        const vm = this;
        axios.get('api/tests')
        .then(function (response){
        console.log(response.data)
        vm.tests = response.data
        })
        }

})