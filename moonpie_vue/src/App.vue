<template>
  <div id="wrapper ">
    <nav class="navbar">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item brand-name">
          <p class="brand-name">MoonPie</p>
        </router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-start">
          <div id="search" class = "navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control">
                  <input type="text" class="input" placeholder="Поиск" name="query">
                </div>
                <div class="control">
                  <button class="button">
                    <span class="icon">
                      <i class="fas fa-search"></i>
                    </span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="navbar-end">
          <router-link to="/" class="navbar-item">Главная</router-link>
          <router-link to="/catalog" class="navbar-item" >Каталог</router-link>
    
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <div class="dropdown is-hoverable">
                 <div class="dropdown-trigger">
                     <router-link to="/my-account" class="navbar-item button">  Личный кабинет  </router-link>
                 </div>
                <div class="dropdown-menu" id="dropdown-menu" role="menu">
                  <div class="dropdown-content">
                    <div class="dropdown-item">
                      <button @click ="logout()" class="button"> Выйти </button>
                    </div>
                  </div>
                  </div>
                </div>
              </template>
              <template v-else>
                <router-link to="/log-in" class="navbar-item button">  Войти  </router-link>
              </template>

              <router-link to="/cart" class="navbar-item button">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span v-if="cartTotalLength>0 "> ({{ cartTotalLength }})  </span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <div class="columns is-multiline has-text-centered">
      <div class="column is-4">
          <p>Контакты:</p>
          <p>Адрес: г. Краснодар, ул. Кореновская, 38</p>
          <p>Телефон: 9 (999) 666 99 66</p>
          <p>E-mail: moonpie@mail.ru</p>
        <br>
          <p>&#169; Kholudeeva Veronika, 2021-2022</p>
      </div>
      <div class="column is-4">
        <router-link to="/" class="navbar-item brand-name">
          <p class="brand-name mt-4 moonpie">MoonPie</p>
        </router-link>
      </div>
      <div class="column is-4">
        <p> Мы в соцсетях</p>
        <router-link to="/"><img class="network" src="../src/assets/pic/vk.png"></router-link>
        <router-link to="/"><img class="network" src="../src//assets/pic/telegram.png"></router-link>
        <router-link to="/"><img class="network" src="../src//assets/pic/youtube.png"></router-link>
      </div>
      </div>
    </footer>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data() {
    return{
      showMobileMenu:false,
      cart:{
        items:[]
      }
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    if (token){
      axios.defaults.headers.common['Authorization']= "Token " + token
    } else {
      axios.defaults.headers.common['Authorization']= ""

    }
  },
  methods:{
    logout(){
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')
            this.$router.push('/')

        },
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed:{
    cartTotalLength(){
      let totalLength = 0

      for (let i=0; i<this.cart.items.length; i++){
        totalLength+=this.cart.items[i].quantity
      }
      return totalLength
    }
  }
}
</script>


<style lang="scss">
@import '../node_modules/bulma';

.moonpie{
  margin:auto;
}
.network{
  width: 50px;
  height: 50px;
  padding: 10px;
}
.footer{
  font-family: 'Gotham Pro';
  background-color:  #201d1ce3;
  height: 210px;
  color:rgb(254, 246, 236);
}

//--------ШРИФТ----

@font-face {
    font-family: 'Gotham Pro';
    src: local('Gotham Pro Light'), local('Gotham-Pro-Light'),
        url('~@/assets/fonts/GothamPro-Light.woff2') format('woff2'),
        url('~@/assets/fonts/GothamPro-Light.woff') format('woff'),
        url('~@/assets/fonts/GothamPro-Light.ttf') format('truetype');
    font-weight: 300;
    font-style: normal;
  }

//-------ШАПКА

.button:hover{
  color: rgb(254, 246, 236);
  background: rgb(0,0,0,0);
}

a.navbar-item:hover{
  color: rgb(254, 246, 236);
  background: rgb(0,0,0,0);
  text-shadow: rgb(249, 244, 225) 1px 0 10px;
}

a.brand-name:hover{
  border:0px;
}

.navbar{
  letter-spacing: 1px;
  font-family: 'Gotham Pro';
  position: absolute;
  width: 100%;
   background-color: rgba(0, 0, 0, 0);
}

.navbar-brand{
  padding-left: 40px;
  padding-right: 40px;
  font-weight: lighter; 
}

.brand-name{
  font-size: 30px;
  color: antiquewhite;
  letter-spacing: 5px;
}

.navbar-item{
  color: antiquewhite;
  padding-left: 20px;
  padding-right: 20px;
  
}

.button, .input{
  height: 30px;
  background: rgb(201, 187, 170, 0);
  border:none;
  color: antiquewhite;
}

.a:active{
  background-color: rgba(0, 0, 0, 0);
}
.navbar-start{
  margin-top: auto;
  margin-bottom: auto;
}

//------ПОИСК
.input::-webkit-input-placeholder {
  color: rgb(201, 187, 170); 
  font-family: 'Gotham Pro';
}
.input:-moz-placeholder {
  color: rgb(201, 187, 170); 
  font-family: 'Gotham Pron';
}
.input:-ms-input-placeholder {
 color: rgb(201, 187, 170); 
  font-family: 'Gotham Pro'; 
}


::-webkit-scrollbar {
  width: 0px;
}

#wrapper{
  background-color: rgb(231, 218, 201);
  color: #1C0800;
  font-family: 'Gotham Pro';
}


.section{
  padding:0;
}

.dropdown-content{
  background-color: #13100fcf;
  text-align: center;
  padding:0;
}

</style>
