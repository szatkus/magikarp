window.addEventListener('load', function () {
  var sample = new Vue({
    el: '#sample',
    data: {
      text: 'loading'
    },
    created: function () {
      setTimeout(function () {
        sample.fetchData();
      }, 2000);
    },
    methods: {
      fetchData: function () {
        fetch('/sample').then(function (response) {
          response.json().then(function (data) {
            sample.text = data.text;
          });
        });
      }
    }
  });
});
