<html>
<head>
<h1>AirBnB_Clone Command Interpreter</h1>
</head>
<body>
<img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="HBnB Logo Part Clone" width="600" height="240" class="center">
<br>
<br>
<h2>Project Description</h2>
<p><strong>In this project we will do the first part of the AirBnB clone final project. In this part we will create the console, where we will create our own data model, manage(create, update, destroy, etc) objects via the console/ command interpreter, and finally store and persist objects to a file (JSON file).</strong></p>
<h2>Command Interpreter Description</h2>
<p>The console allows you to manage your objects with the following commands:</p>
<table>
<tr>
<th>Command</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>create</td>
<td>Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id</td>
<td><code>$ create BaseModel</code></td>
</tr>
<tr>
<td>show</td>
<td>Prints the string representation of an instance based on the class name and id</td>
<td><code>$ show BaseModel 1234-1234-1234</code></td>
</tr>
<tr>
<td>destroy</td>
<td>Deletes an instance based on the class name and id</td>
<td><code>$ destroy BaseModel 1234-1234-1234</code></td>
</tr>
<tr>
<td>all</td>
<td>Prints all string representation of all instances based or not on the class name</td>
<td><code>$ all BaseModel or $ all</code></td>
</tr>
<tr>
<td>update</td>
<td>Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)</td>
<td><code>$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"</code></td>
</tr>
</table>
<h2>How to start it</h2>
<p>First you have to clone the rep, so you have to execute the following command:</p>
<p style="background-color:A7A4A4;"><code>git clone https://github.com/DanielBaquero28/AirBnB_clone.git</code></p>
<p>Then access the repo by changing your directory to "AirBnB_clone":</p>
<p style="background-color:A7A4A4;"><code>cd AirBnB_clone</code></p>
<p>Now execute the file named "console.py":</p>
<p style="background-color:A7A4A4;"><code>./console.py</code></p>
<h2>How to use it</h2>
<h2>Interactive Mode</h2>
<p>To enter the interative mode you must execute the following command</p>
<p style="background-color:A7A4A4;"><code>./console.py
<br>
(hbnb)</code>
</p>
<h2>Non Interactive Mode</h2>
<p>To use the non-interactive mode you must use the echo command with the instructions you want to execute, then pipe it executing the name of the file "console.py"</p>
<p style="background-color:A7A4A4;"><code>echo "create BaseModel" | ./console</code></p>
<h2>Examples</h2>
<p>The following are some examples of the console:</p>
<h3>Create</h3>
<p style="background-color:A7A4A4;"><code>(hbnb) create BaseModel</code>
<br>
<code>2386ef96-9d7f-4914-8885-4076afdf9e84</code>
<br>
<code>(hbnb)</code>
</p>
<br>
<h3>Show</h3>
<p style="background-color:A7A4A4;"><code>(hbnb) show BaseModel 2386ef96-9d7f-4914-8885-4076afdf9e84</code>
<br>
<code>[BaseModel] (2386ef96-9d7f-4914-8885-4076afdf9e84) {'id': '2386ef96-9d7f-4914-8885-4076afdf9e84', 'updated_at': datetime.datetime(2019, 11, 13, 23, 48, 10, 468818), 'created_at': datetime.datetime(2019, 11, 13, 23, 48, 10, 468774)}</code>
<br>
<code>(hbnb)</code>
</p>
<br>
<h3>Update</h3>
<p style="background-color:A7A4A4;"><code>(hbnb) update BaseModel 2386ef96-9d7f-4914-8885-4076afdf9e84 user Daniel</code>
<br>
<code>(hbnb) show BaseModel 2386ef96-9d7f-4914-8885-4076afdf9e84</code>
<br>
<code>[BaseModel] (2386ef96-9d7f-4914-8885-4076afdf9e84) {'id': '2386ef96-9d7f-4914-8885-4076afdf9e84', 'updated_at': datetime.datetime(2019, 11, 13, 23, 48, 10, 468818), 'created_at': datetime.datetime(2019, 11, 13, 23, 48, 10, 468774)}</code>
<br>
<code>(hbnb)</code>
</p>
<br>
<h3>Destroy</h3>
<p style="background-color:A7A4A4;"><code>(hbnb) destroy BaseModel 2386ef96-9d7f-4914-8885-4076afdf9e84</code>
<br>
<code>(hbnb) show BaseModel 2386ef96-9d7f-4914-8885-4076afdf9e84</code>
<br>
<code>** no instance found **</code>
<br>
<code>(hbnb)</code>
</p>
<br>
<h3>All</h3>
<p style="background-color:A7A4A4;"><code>(hbnb) all</code>
<br>
<code>{'BaseModel.c94db76d-a8bf-4a73-b8d0-7272900863a1': <models.base_model.BaseModel object at 0x7f4d49d42198>, 'BaseModel.22e40cd7-1a74-4f22-87df-cfcc219c3a28': <models.base_model.BaseModel object at 0x7f4d49128e48>, 'BaseModel.3d3da26f-4fba-41e4-bd04-4d4d92d8fd86': <models.base_model.BaseModel object at 0x7f4d49128f98>, 'BaseModel.97cfbdc7-82cf-4739-8a9f-bc1c47b5cfe2': <models.base_model.BaseModel object at 0x7f4d49d42320>, 'State.4143fd08-2ab9-4d46-8a79-b76a412ee3e1': <models.state.State object at 0x7f4d49d422e8>, 'BaseModel.651c43d2-755f-47ef-aed4-c68386b87a44': <models.base_model.BaseModel object at 0x7f4d49128eb8>, 'BaseModel.535809cb-4f9f-46b9-9ca0-21829bd2b423': <models.base_model.BaseModel object at 0x7f4d49128ef0>, 'BaseModel.134f0950-4a69-4225-9787-14cc1176533c': <models.base_model.BaseModel object at 0x7f4d49128e80>, 'BaseModel.8d8fc58d-811f-408e-b633-fc07105c09eb': <models.base_model.BaseModel object at 0x7f4d49128f60>, 'BaseModel.22f749e1-4cb2-4de8-b828-3f426c1fb5cd': <models.base_model.BaseModel object at 0x7f4d49d42358>, 'BaseModel.d12005fc-5325-4aab-a2d1-8a717ae5c0cf': <models.base_model.BaseModel object at 0x7f4d490fe320>, 'State.184d8a5b-d4d7-4f9e-8579-0e906b119700': <models.state.State object at 0x7f4d49d42240>, 'BaseModel.48d455da-2c90-4195-b9e4-be9ff061d029': <models.base_model.BaseModel object at 0x7f4d49128f28>}</code>
<br>
<code>(hbnb)</code>
</p>
<h2>Managing Classes</h2>
<p>We will manage the following classes:</p>
<ul>
<li>User</li>
<li>State</li>
<li>City</li>
<li>Amenity</li>
<li>Place</li>
<li>Review</li>
</ul>
</body>
<footer>
Made by: <strong><a href="https://github.com/Skillhh">Giovanny Andres Ortegon Espitia</a>, <a href="https://github.com/DanielBaquero28">Daniel Baquero</a>, <a href="https://github.com/arq-gabo">José Gabriel Guerra</a></strong>
</footer>
</html>
