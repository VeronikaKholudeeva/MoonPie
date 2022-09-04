<template>
<div class="my-page">
    <div class="blur-wrapper">
    <div class="hero is-fullheight page-log-in">
        <div class="hero is-fullheight columns log-in">
            <div class="column is-4 is-offset-4">
                <h1 class="is-size-3 has-text-centered">Вход</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label> Логин: </label>
                        <div class = "control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label> Пароль: </label>
                        <div class = "control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <div class="field">
                        <div class = "control has-text-centered">
                            <button class="button is-dark">Войти</button>
                        </div>
                    </div>
                    <hr>
                    Или нажмите, чтобы <router-link to="/sign-up">Зарегистрироваться</router-link>
                </form>
            </div>
        </div>
    </div>
    </div>
</div>
</template>

<script>

import axios from 'axios'
import {toast} from 'bulma-toast'

export default{
    name: 'LogIn',
    data(){
        return{
            username: '',
            password:'',
            errors:[]
        }
    },
    mounted(){
        document.title = 'Вход | MoonPie'

    },
    methods:{
        async submitForm(){

            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            const formData={
                 username: this.username,
                 password: this.password
            }
            await axios
                    .post("/api/v1/token/login/", formData)
                    .then(response =>{
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = "Token " +token

                        localStorage.setItem("token", token)

                        const toPath = this.$route.query.to || '/cart'

                        this.$router.push(toPath)
                    })
                .catch( error =>{
                    if (error.response){
                        for(const property in error.response.data){
                            this.errors.push(`${property}:${error.response.data[property]}`)
                        }

                        console.log(JSON.stringify(error.response.data))
                    }else if (error.message){
                        this.errors.push('Что-то пошло не так. Пожалуйста, попробуйте еще раз')
                        console.log(JSON.stringify(error))
                    }
                    
                })
            
        }
    }
}
</script>
<style scoped>
.page-log-in{
    font-family:'Gotham Pro';
    padding-top:80px;
}
.log-in{
    padding: 50px;
    padding-top: 30px;
    background-color: rgb(255, 247, 242);
}
h1{
    margin-bottom: 20px;
}
input{
    color:black;
    background-color: rgb(248, 238, 232);
}
</style>