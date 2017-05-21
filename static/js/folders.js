window.addEventListener('load', function () {
  var folders = new Vue({
    el: '#folders',
    data: {
      fetched: false,
      newFolder: "",
      currentFolder: '-1', // -1 jest traktowany jako katalog glowny
      data_in_json: ''
    },
    created: function () {
      setTimeout(function () {
        folders.fetchData();
      }, 20000);
    },
    methods: {
      fetchData: function () {
        fetch('/folders_json').then(function (response) {
          response.json().then(function (data) {
              folders.data_in_json = data;
              folders.fetched = true;
          });
        });
      },
      delete_folder: function (folder) {
          var index = folders.data_in_json[folders.currentFolder].indexOf(folder);
          folders.data_in_json[folders.currentFolder].splice(index, 1);
          console.log('Usunieto folder ', folder.description);
      },
      add_folder: function () {
          var new_folder = folders.newFolder.trim();
          if (new_folder) {
              folders.data_in_json[folders.currentFolder].push({ 'description': new_folder });
          };
          folders.newFolder = "";
          console.log('Dodano folder ', new_folder);
      },
      nest: function (folder) {
          //folders.currentFolder = folder.folder_id;
          console.log('Rozszerzono folder ', folder.description);
      },
      reset_current_folder: function () {
          folders.currentFolder = '-1';
      }
    }
  });
});

