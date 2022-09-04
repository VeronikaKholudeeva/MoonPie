<template>
<div class="my-page">
    <div class="blur-wrapper">
    <div class="hero is-fullheight cart-page">
        <div class = "column is-multiline cart">
            <div class="column is-12">
                <h1 class="is-size-2 has-text-centered">Корзина</h1>
            </div>
            <div class="column is-12 box"  v-if="cartTotalLength">
                <table class = "table is-fullwidth">
                    <thead>
                        <tr>
                            <th> Наименование</th>
                            <th class="has-text-centered"> Цена</th>
                            <th class="has-text-centered"> Количество</th>
                            <th class="has-text-centered"> Сумма</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart" />
                    </tbody>
                    <tfoot>
                        <tr>
                            <th scope="row" colspan="2">Cумма</th>
                            <th class="has-text-centered">{{cartTotalLength}}</th>
                            <th class="has-text-centered">{{ cartTotalPrice.toFixed(2)}} руб.</th>
                        </tr>
                    </tfoot>
                </table>
                <div class="butt">
                <router-link to="/cart/checkout" class="button is-dark">Заказать</router-link>
                </div>
            </div>
            <p v-else>У вас нет товаров в корзине..</p> 
            
        </div>
    </div>
    </div>
</div>
</template>

<script>

import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
    name: "Cart",
    components:{
        CartItem
    },
    data(){
        return{
            cart:{
                items:[]
            }
        }
    },
    mounted(){
        this.cart = this.$store.state.cart
    },
    methods:{
        removeFromCart(item){
            this.cart.items=this.cart.items.filter(i=>i.product.id !== item.product.id)
        }
    },
    computed:{
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)  =>{
                return acc+=curVal.quantity
            },0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal)  =>{
                return acc+=curVal.product.price * curVal.quantity
            },0)
        }
    }
}
</script>
<style scoped>
.cart-page{
    font-family:'Gotham Pro';
    padding-top:68px;
    
}
.cart{
    padding: 50px;
    padding-top: 30px;
    background-color: rgb(255, 247, 242);
}
h1{
   
    margin-bottom: 20px;
}
.box{
        box-shadow: rgba(0, 0, 0, 0.45) 10px 10px 10px -10px;

    }
h2{
    color: black;
    margin-bottom: 10px;
}
.butt{
    text-align: center;
}
</style>