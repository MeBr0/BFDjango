# KBTU 2020 Spring

## Todo laboratory work

Simple todo list

### Documentation

Template and description of methods of following api
  
#### Auth

##### Register
* `POST /auth/register`
   
* Body parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |username|String|yes|Unique|
  |password|String|yes||
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |201|`{"id": 7,"username": "mebr7","is_superuser": false}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |400|`{"username": ["This field may not be null."]}`|
   |400|`{"password": ["This field may not be null."]}`|
   |400|`{"username": ["This field is required."]}`|
   |400|`{"password": ["This field is required."]}`|
   |400|`{"username": ["A user with that username already exists."]}`|
 
##### Login
* `POST /auth/login`
   
* Body parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |username|String|yes||
  |password|String|yes||
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |200|`{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |400|`{"username": ["This field may not be null."]}`|
   |400|`{"password": ["This field may not be null."]}`|
   |400|`{"username": ["This field is required."]}`|
   |400|`{"password": ["This field is required."]}`|
   |400|`{"non_field_errors": ["Unable to log in with provided credentials."]}`|

##### Authorization
Next methods require authorization. That how authorization can be applied

* Header parameters

  |Key|Value|
  |:----|:---:|
  |Authorization|JWT _{{Token}}_|
  
  * _Token from login method_
  
* Possible error responses
   
   |Code|Content|
   |:---:|:---:|
   |401|`{"detail": "Authentication credentials were not provided."}`|
   |401|`{"detail": "Invalid Authorization header. No credentials provided."}`|
  
#### Lists

##### Get all lists
* `GET /lists`
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |200|`[{"id": 6,"name": "qwe2","owner": {"id": 1,"username": "mebr0","is_superuser": true}}]`|
   
##### Create new list
* `POST /lists`
  
* Body parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |name|String|yes||
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |201|`{"id": 9,"name": "qwe","owner": {"id": 1,"username": "mebr0","is_superuser": true}}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |400|`{"name": ["This field may not be null."]}`|
   |400|`{"name": ["This field is required."]}`|
   |400|`{"name": ["This field may not be blank."]}`|
   
##### Get list
* `GET /lists/:id`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |200|`{"id": 9,"name": "qwe","owner": {"id": 1,"username": "mebr0","is_superuser": true}}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |404|`{"detail": "Not found."}`|
   
##### Update list
* `PATCH /lists/:id`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|

* Body parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |name|String|no|New name|

* Success response

   |Code|Content|
   |:---:|:---:|
   |200|`{"id": 9,"name": "qwer","owner": {"id": 1,"username": "mebr0","is_superuser": true}}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |400|`{"name": ["This field may not be null."]}`|
   |400|`{"name": ["This field is required."]}`|
   |400|`{"name": ["This field may not be blank."]}`|
   |404|`{"detail": "Not found."}`|
   
##### Delete list
* `DELETE /lists/:id`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|

* Success response

   |Code|Content|
   |:---:|:---:|
   |204||
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |404|`{"detail": "Not found."}`|
   
#### Tasks

##### Get all tasks from list
* `GET /lists/:id/todo`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |200|`[{"id": 8,"name": "qwe","created_at": "2020-03-25T11:07:15.626297Z","due_on": null,"is_done": false,"list": {"id": 6,"name": "qwe2","owner": {"id": 1,"username": "mebr0","is_superuser": true}},"notes": "eqweqwe"}]`|
   
##### Create new task in list
* `POST /lists/:id/todo`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|
  
* Body parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |name|String|yes||
  |created_at|Datetime|no|Date and time created|
  |due_on|Datetime|no|Due on date|
  |is_done|boolean|no|Done attribute|
  |notes|String|no|Notes related to task|
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |201|`{"id": 15,"name": "qwe","created_at": "2020-03-25T12:59:08.992821Z","due_on": null,"is_done": false,"list": {"id": 6,"name": "qwe2","owner": {"id": 1,"username": "mebr0","is_superuser": true}},"notes": ""}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |400|`{"name": ["This field may not be null."]}`|
   |400|`{"name": ["This field is required."]}`|
   |400|`{"name": ["This field may not be blank."]}`|
   |400|`{"created_at": ["This field may not be null."]}`|
   |400|`{"created_at": ["Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuu]]."]}`|
   |400|`{"due_on": ["Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuu]]."]}`|
   |400|`{"is_done": ["This field may not be null."]}`|
   |400|`{"notes": ["This field may not be null."]}`|
   
##### Get task in list
* `POST /lists/:id/todo/:t_id`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|
  |t_id|Path|yes|Id of task|
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |200|`{"id": 8,"name": "qwe","created_at": "2020-03-25T11:07:15.626297Z","due_on": null,"is_done":false,"list": {"id": 6,"name": "qwe2","owner": {"id": 1,"username": "mebr0","is_superuser": true}},"notes": "eqweqwe"}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |404|`{"detail": "Not found."}`|
   
##### Update task in list
* `PATCH /lists/:id/todo/:t_id`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|
  |t_id|Path|yes|Id of task|
  
* Body parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |name|String|yes||
  |created_at|Datetime|no|Date and time created|
  |due_on|Datetime|no|Due on date|
  |is_done|boolean|no|Done attribute|
  |notes|String|no|Notes related to task|
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |200|`{"id": 15,"name": "qwer","created_at": "2020-03-25T12:59:08.992821Z","due_on": null,"is_done": false,"list": {"id": 6,"name": "qwe2","owner": {"id": 1,"username": "mebr0","is_superuser": true}},"notes": ""}`|
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |400|`{"name": ["This field may not be null."]}`|
   |400|`{"name": ["This field may not be blank."]}`|
   |400|`{"created_at": ["This field may not be null."]}`|
   |400|`{"created_at": ["Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuu]]."]}`|
   |400|`{"due_on": ["Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuu]]."]}`|
   |400|`{"is_done": ["This field may not be null."]}`|
   |400|`{"notes": ["This field may not be null."]}`|
   |404|`{"detail": "Not found."}`|
   
##### Delete task in list
* `DELETE /lists/:id/todo/:t_id`
   
* URL parameters

  |Name|Type|Required|Description|
  |:----|:---:|:---:|:---|
  |id|Path|yes|Id of list|
  |t_id|Path|yes|Id of task|
  
* Success response

   |Code|Content|
   |:---:|:---:|
   |204||
   
* Other responses
   
   |Code|Content|
   |:---:|:---:|
   |404|`{"detail": "Not found."}`|