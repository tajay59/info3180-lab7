<template>
<div class="container">
    <form @submit.prevent="uploadPhoto" id="uploadForm">
        <label for="description">Photo Description</label>
        <textarea name="description" id="description" cols="30" rows="10"></textarea>
        <br>
        <label for="photo">File</label>
        <input type="file" id="photo" name="photo">
        <button type="submit">Send</button>
    
    </form>
</div>
       
</template>

<script>
export default {
    data() {
      return {
          csrf_token: '',
          year: (new Date).getFullYear()
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

            let uploadForm = document.querySelector("#uploadForm")
            let form_data = new FormData(uploadForm);

            fetch("/api/upload", { method: 'POST',body: form_data,headers: {'X-CSRFToken': this.csrf_token}})
            .then(function (response) {
            return response.json();
            })
            .then(function (data) {
            // display a success message
            console.log(data);
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
</style>