<html>
  <head>
    <title>Wakamonog Demo Script</title>
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="//bootswatch.com/cerulean/bootstrap.min.css">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
  </head>
  <body>
    <div class="navbar navbar-default">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">Wakamonog Sample</a>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="panel panel-primary">
          <div class="panel-heading">Loading result</div>
          <div class="panel-body">
            <table class="table table-striped table-hover">
              <thead>
                <tr>
                  <th>Num</th>
                  <th>Name</th>
                  <th>Sex</th>
                  <th>Mail</th>
                  <th>Birthday</th>
                </tr>
              </thead>
              <tbody>
	        #for $row in $data
	        <tr>
	          <td>$row[0]</td>
	          <td>$row[1]</td>
		  <td>$row[2]</td>
	          <td>$row[3]</td>
	          <td>$row[4]</td>
	        </tr>
                #end for
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
