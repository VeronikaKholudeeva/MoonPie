<template>
<div class="my-page">
    <div class="blur-wrapper">
  <div class="hero is-fullheight page-my-account">
      <div class=" columns is-multiline account">
          <div class="column is-12 has-text-centered">
              <h1 class="is-size-2">Личный кабинет </h1>
          

          
              
          </div>
          <hr>

          <div class="column is-12">
              <h2 class="is-size-5  has-text-centered">Мои заказы</h2>
              <OrderSummary
              v-for="order in orders"
              v-bind:key="order.id"
              v-bind:order="order"/>
          </div>
      </div>
  </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'


import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'MyAccount',
    components:{
        OrderSummary
    },
    data(){
        return{
            orders:[]
        }

    },
    mounted(){
        document.title = 'Личный кабинет | MoonPie'
        this.getMyOrders()
    },
    methods:{
        
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)
        
            await axios
                .get('/api/v1/orders/')
                .then( response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style lang="scss">
.page-my-account{
    padding-top:80px;
    font-family:'Gotham Pro';
}
.account{
    padding: 50px;
    background-color: rgb(255, 247, 242);
}
.my-page{
    background-image: url("../assets/pic/background.jpg");
    
}
.blur-wrapper{
    background-color: rgba(3, 1, 0, 0.696);
    backdrop-filter: blur(10px);
    
}
.title, .subtitle{
    color:rgba(229, 215, 198, 0.774);
}
.hero button{
    font-size: 20px;
    
}
h1{
  margin-top:-20px;
}
h2{
    margin-bottom:20px;
    
}
</style>