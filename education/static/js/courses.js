new Vue({
    el: '#id_courses',
    data: {
    courses: []
    },
    created: function () {
        const vm = this;
        axios.get('api/courses')
        .then(function (response){
        console.log(response.data)
        vm.courses = response.data
        })
    }
}
)