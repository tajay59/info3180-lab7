<template>
<div class="container">
    <h1>Upload Form</h1>
    <ul class="errormessages" :class="{danger:errormessage, success:successmessage}">
        <li v-for="message in messages">{{message}}</li>
    </ul>
    <form @submit.prevent="uploadPhoto" id="uploadForm">
        <label for="description">Description</label>
        <textarea name="description" id="description" cols="30" rows="1"></textarea>
        <br>
        <label for="photo">Photo Upload</label>
        <input type="file" id="photo" name="photo">
        <button type="submit">Send</button>
    
    </form>
</div>
       
</template>

<script>
export default {
    data() {
      return {
          errormessage:false,
          successmessage:false,
          csrf_token: '',
          year: (new Date).getFullYear(),
          messages:[]
      }        
    },
    created() {
    this.getCsrfToken();
    },
    methods: {
        getCsrfToken(){
            let self = this;
            fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                });
        },
        uploadPhoto(){
            console.log("uploadPhoto func called");
            let self = this
            let uploadForm = document.querySelector("#uploadForm")
            let form_data = new FormData(uploadForm);
            console.log(form_data);

            fetch("/api/upload", { method: 'POST',body: form_data,headers: {'X-CSRFToken': this.csrf_token}})
            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            // display a success message
            let res = Object.keys(data);
            if(res.includes("errors")){
                console.log("messages errors")
                self.errormessage = true;
                self.successmessage = false;
                self.messages.splice(0,self.messages.length);
                console.log(data["errors"]); 
                data["errors"].forEach((el)=>{
                    self.messages.push(el)
                });
            }else if(data["message"].includes("successful")){
                console.log("messages successful");
                self.errormessage = false;
                self.successmessage = true;
                self.messages.splice(0,self.messages.length);
                self.messages.push("File upload successful")
                
            }
                
            })
            .catch(function (error) {
            console.log(error);
                    })
                }
}
}
</script>

<style>
/* Add any component specific styles here */

*{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
.container{
    display: grid;
    grid-template-columns: 1fr;
    grid-auto-rows: auto;
}

form{
    display: flex;
    flex-direction: column;
    width: 400px;
    justify-self: center;
    align-self:center;
}
h1{
    justify-self: center;
}

.danger{
    background-color: lightcoral;
    border: none;
    border-radius: 5px;
    padding: 5px;
    padding-left: 20px;
}

.success{
    background: lightseagreen;
    color:white;
    border: none;
    border-radius: 5px;
    padding: 5px;
    padding-left: 20px;
}
ul{
    justify-self: center;
    width: 400px;
}

li{
list-style: none;
}
</style>