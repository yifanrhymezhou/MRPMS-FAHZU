$(document).ready(function () {
  var table
  function addProject(data) {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "project_summaries",
      "method": "POST",
      "headers": {
      "content-type": "application/json",
      "cache-control": "no-cache",
      "postman-token": "2612534b-9ccd-ab7e-1f73-659029967199"
        },
      "processData": false,
      "data": JSON.stringify(data)
}
      $.ajax(settings).done(function (response) {
          $('.modal.in').modal('hide')
          $.notify("Project record has been added successfully!", {"status":"success"});
          table.destroy();
          $('#datatable4 tbody').empty(); // empty in case the columns change
          getProject()
      });
    }

  function deleteProject(id) {
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "project_summaries/" + id,
      "method": "delete",
      "headers": {
          "cache-control": "no-cache",
          "postman-token": "28ea8360-5af0-1d11-e595-485a109760f2"
      }
    }
    swal({
        title: "Are you sure?",
        text: "You will not be able to recover this data",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, delete it!",
        closeOnConfirm: false
    }, function() {
        $.ajax(settings).done(function (response) {
          swal("Deleted!", "Project record has been removed.", "success");
          table.destroy();
          $('#datatable4 tbody').empty(); // empty in case the columns change
          getProject()
        }); 
    });
  }
    function updateProject(data, ID) {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "project_summaries/" + ID,
            "method": "PUT",
            "headers": {
                "content-type": "application/json",
                "cache-control": "no-cache"
            },
            "processData": false,
            "data": JSON.stringify(data)
        }

        $.ajax(settings).done(function (response) {
            $('.modal.in').modal('hide')
            $.notify("Project Updated Successfully", {"status":"success"});
            table.destroy();
            $('#datatable4 tbody').empty(); // empty in case the columns change
            getProject()
        });


    }
    function getProject() {
        var settings = {
            "async": true,
            "crossDomain": true,
            "url": "project_summaries",
            "method": "GET",
            "headers": {
                "cache-control": "no-cache"
            }
        }
        $.ajax(settings).done(function (response) {
            table = $('#datatable4').DataTable({
                "bDestroy": true,
                'paging': true, // Table pagination
                'ordering': true, // Column ordering
                'info': true, // Bottom left status text
                aaData: response,
                 "aaSorting": [],
                aoColumns: [
                    {
                      mData: 'ID'
                    },
                    {
                      mData: 'PROJ_ID'
                    },
                    {
                      mData: 'NAME'
                    },
                    {
                      mData: 'MANAGEMENT'
                    },
                    {
                      mData: 'START_DATE'
                    },
                    {
                      mData: 'END_DATE'
                    },
                    {
                      mData: 'IS_COMPLETED'
                    },
                    {
                      mData: 'IS_EXPAND_DATE'
                    },
                    {
                      mData: 'NEW_END_DATE'
                    },
                    {
                      mData: 'DELAY_REMARK'
                    },
                    {
                      mRender: function (o) {
                          return '<button class="btn btn-success btn-edit" id="btn-edit" type="button" style="border-radius:10%;">Update</button> <button class="btn btn-danger delete-btn" id="delete-btn" type="button" style="border-radius:10%;">Remove</button>';
                      }
                    },                  
                  ]     
                });
              });
    }

    $("#addproject").click(function () {
      console.log('hey')
      $('#detailform input,textarea').val("")
      $('#myModal').modal().one('shown.bs.modal', function (e) {
        console.log('innn')
        $("#savethepatient").off("click").on("click", function(e) {
          console.log("inn2")
          var instance = $('#detailform').parsley();
          instance.validate()
          if(instance.isValid()){
            var jsondata = $('#detailform').serializeJSON();
            console.log(jsondata)
            addProject(jsondata)
          }
        })
      })
    })

    $('#datatable4').on('click', '#delete-btn', function () {
      /*DEFINE THE TABLE!*/
      var table = $('#datatable4').DataTable();
      data = table.row($(this).parents('tr')).data();
      console.log(data)
      deleteProject(data.ID)
    });

    $('#datatable4').on('click', '#btn-edit', function (e) {
      var table = $('#datatable4').DataTable();
      /*DEFINE THE TABLE!*/
      data = table.row($(this).parents('tr')).data();
      console.log(data)
      for (var key in data) {
        console.log(key)
        $("#detailform input[name='"+ key+ "']").val(data[key])
      }
      $('#myModal').modal().one('shown.bs.modal', function (e) {
        $("#savethepatient").off("click").on("click", function(e) {
        var instance = $('#detailform').parsley();
        instance.validate()
        console.log(instance.isValid())
        if(instance.isValid()){
            jsondata = $('#detailform').serializeJSON();
            updatePatient(jsondata, data.pat_id)
            }
        })
    })
  });

getProject()
})