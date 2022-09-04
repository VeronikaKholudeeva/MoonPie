<template>
    <div class="my-page">
    <div class="blur-wrapper">
    <div class="page-checkout">
        <div class="columns is-multiline check">
            <div class="column is-12">
                <h1 class="is-size-3"> Подтверждение заказа </h1>
            </div>
            <div class="column is-12 box">
                <table class ="table is-fullwidth">
                    <thead>
                        <tr>
                            <th> Наименование</th>
                            <th> Цена</th>
                            <th> Количество</th>
                            <th> Сумма</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr 
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                        <td>{{ item.product.name }}</td>
                        <td> {{ item.product.price }} руб.</td>
                        <td> {{ item.quantity }}</td>
                        <td> {{ getItemTotal(item).toFixed(2) }} руб.</td>
                        </tr>
                    </tbody> 
                    <tfoot>
                        <tr>
                            <td colspan="2">Итог: </td>
                            <td> {{ cartTotalLength}}</td>
                            <td> {{ cartTotalPrice.toFixed(2) }} руб. </td>
                        </tr>
                    </tfoot>   
                </table>
            </div>
            <div class="column is-12 box">
                <h2 class="is-size-4"> Детали заказа </h2>
                <p class="has-text-grey mb-4"> * Все поля являются обязательными для заполнения </p>
                
                <div class="column is-multiline">
                    <div class="column is-6">
                        
                        <div class="field">
                            <label> Имя* </label>
                            <div class = "control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>
                        <div class="field">
                            <label> Фамилия* </label>
                            <div class = "control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>
                        <div class="field">
                            <label> E-mail* </label>
                            <div class = "control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>
                        <div class="field">
                            <label> Телефон* </label>
                            <div class = "control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>
                        <div class="column is-6">
                            <div class="field">
                                <label> Адрес* </label>
                                <div class = "control">
                                    <input type="text" class="input" v-model="address">
                                </div>
                            </div>
                        </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <hr>
                    <div id="card-element" class="mb-5"></div>
                    <template v-if="cartTotalLength">
                        <hr>

                        <p class="button is-dark" @click="submitForm">Оплатить</p>
                    </template>
                    
                </div> 
                
            </div>
            
        </div>
    </div>
    </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data(){
        return{
            cart: {
                items:[]
            },
            stripe:{},
            card:{},
            first_name:'',
            last_name:'',
            email:'',
            phone:'',
            address:'',
            errors:[]
        }
    },
    mounted(){
        document.title = 'Checkout | MoonPie'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength>0){
            this.stripe = Stripe('pk_test_51Kwn4CI8cGcXSVw4U2OJojuAtGxn5CXYlvg0QBHWxhGWdKnY0o01ps0CkI6uaCABYEqgMrElSvtfSKw3uiuo0gAm00pdY2mxgj')
            const elements = this.stripe.elements();
            this.card = elements.create('card', {hidePostalCode: true})
            this.card.mount('#card-element')
        }
    },
    methods:{
        getItemTotal(item){
            return item.quantity *item.product.price
        },

        submitForm(){
            this.errors = []
            if (this.first_name ===''){
                this.errors.push(' Введите имя')
            }
            if (this.last_name ===''){
                this.errors.push('Введите фамилию')
            }
            if (this.email ===''){
                this.errors.push(' Введите e-mail')
            }
            if (this.address ===''){
                this.errors.push('Введите адрес')
            }
            if (this.phone ===''){
                this.errors.push('Введите телефон')
            }
            if (!this.errors.length){
                this.$store.commit('setIsLoading', true)
                this.stripe.createToken(this.card).then(result => {
                    if (result.error){
                        this.$store.commit('setIsLoading', false)
                        this.errors.push('Что-то пошло не так, пожалуйста, попробуйте снова')
                        console.log(result.error.message)
                    } else{
                        this.stripeTokenHandler(result.token)
                    }
                })
                
            }
        },
        async stripeTokenHandler(token){
            const items = []

            for (let i=0; i<this.cart.items.length; i++){
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price *item.quantity
                }

                items.push(obj)
            }

            const data={
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email':this.email,
                'address': this.address,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id,
            }

            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Что-то пошло не так. Пожалуйста, поробуйте снова')
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
        }
    },


    computed:{
        
        cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal)  =>{
                return acc+=curVal.product.price * curVal.quantity
            },0)
        },
        cartTotalLength(){
            return this.cart.items.reduce((acc, curVal) =>{
                return acc += curVal.quantity
            }, 0)
        }
    
    }
}
</script>
<style scoped>
.page-checkout{
    font-family:'Gotham Pro';
    padding-top:80px;
}
.check{
padding: 50px;
    padding-top: 30px;
    background-color: rgb(255, 247, 242);
}
.box{
    box-shadow: rgba(0, 0, 0, 0.45) 10px 10px 10px -10px;
    }
input{
    background-color: rgb(255, 247, 242);
    color:black;
}
</style>