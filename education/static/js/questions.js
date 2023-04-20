new Vue({
    el: '#id_questions',
    data: {
    questions: []
    },
    created: function () {
        const vm = this;
        axios.get('api/questions')
        .then(function (response){
        console.log(response.data)
        vm.questions = response.data
        })
        }

})