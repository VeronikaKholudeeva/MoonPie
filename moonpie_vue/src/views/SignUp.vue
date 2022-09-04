<template>
    <div class="my-page">
    <div class="blur-wrapper">
    <div class="hero is-fullheight page-sign-up">
        <div class="hero is-fullheight columns is-multiline sign-up">
            <div class="column is-4 is-offset-4">
                <h1 class="is-size-3 has-text-centered">Зарегистрироваться</h1>
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
                    <div class="field">
                        <label> Повторите пароль: </label>
                        <div class = "control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <div class="field">
                        <div class = "control has-text-centered">
                            <button class="button is-dark">Зарегистрироваться</button>
                        </div>
                    </div>
                    <hr>
                    Или нажмите, чтобы <router-link to="/log-in">Войти</router-link>
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
    name: 'SignUp',
    data(){
        return{
            username: '',
            password:'',
            password2:'',
            errors:[]
        }
    },
    methods:{
        submitForm(){
            this.errors = []
            if (this.username ===''){
                this.errors.push('Введите логин')
            }
            if (this.password ===''){
                this.errors.push('Введите пароль')
            }
            if (this.password!== this.password2){
                this.errors.push('Пароли не совпадают')
            }

            if (!this.errors.length){
                const formData={
                    username: this.username,
                    password: this.password
                }
                axios
                    .post("/api/v1/users/", formData)
                    .then(response =>{
                        toast({
                            message: "Аккаунт создан, пожалуйста, войдите",
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/log-in')
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
}
</script>
<style scoped>
.page-sign-up{
    font-family:'Gotham Pro';
    padding-top:80px;
}
.sign-up{
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