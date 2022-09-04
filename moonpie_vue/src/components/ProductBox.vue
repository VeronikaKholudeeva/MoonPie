<template>
    <div class="column ">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="product.get_thumbnail">
              </figure>
              <p class="name is-size-5">{{ product.name }}</p>
              <p class="is-size-6 has-text-grey">{{ product.price }} руб.</p>
              <div class="box-foot">
                <button class="button mt-4" @click="isActive=true">Добавить в корзину</button>
              </div>
        </div>


        <div class="modal is-active act" v-show="isActive">
            <div class="modal-background"></div>
            <div class="modal-card">
                <header class="modal-card-head">
                    <p class="modal-card-title has-text-centered">{{ product.name }}</p>
                    <button class="delete" @click="isActive=false" aria-label="close"></button>
                </header>
                <section class="modal-card-body">
                    <figure class='image mb-4'>
                        <img v-bind:src="product.get_image">
                    </figure>
                   
                    <p><strong>Цена: </strong>{{ product.price }} руб</p>
                    <p><strong>Вес: </strong>{{ product.weight }} г</p>
                    <p>{{ product.description }}</p>
                </section>
                <footer class="modal-card-foot">
                    <div class="field has-addons card-foot">
                        <div class="control">
                            <input type="number" class="input" min="1" v-model="quantity">
                        </div>

                        <div class="control">
                            <a class="button add-cart" @click='addToCart'>Добавить в корзину</a>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'ProductBox',
    props:{
        product:Object,
        isActive: {
            type: Boolean,
            default: false
        },
        quantity:{
            type: Number,
            default: 1
        }
    },
    methods:{
        addToCart(){
            console.log('addToCart')
            if (isNaN(this.quantity)||this.quantity<1){
                this.quantity=1
            }

            const item={
                product:this.product,
                quantity:this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'Товар добавлен в корзину',
                type: 'is-success',
                dismissible:true,
                pauseOnHover:true,
                duration:2000,
                position:'bottom-right',
            })
        }
    }
    
}
</script>
<style scoped>
    .image{
     
    }
    img{
        
        
    }
    .box{
       font-family:'Gotham Pro'; 
    }
    .modal-card-foot{
        height: 60px;
    }
    .card-foot{
     margin:auto;   
        
    }
   
    .name{
        height: 70px;
    }
    a{
        color: #1C0800;
    }
    .title{
        color: #1C0800; 
    }
    .button{
         margin: auto;
    }
    .input{
        border-radius: 20px;
        text-align: center;
    }
    .box-foot{
        text-align: center;

    }
    .box p{
        text-align: center;
        padding:0;
    }
    .button, .input{
        font-family:'Gotham Pro';
        font-size: 18px;
        color:antiquewhite;
        border-radius: 3px;
        background-color: #201d1cbb;
        padding:10px;
    }
     .input{
        background-color: white;
        color: #1C0800;
    }
    .box{
        box-shadow: rgba(0, 0, 0, 0.45) 10px 10px 10px -10px;

    }
    .act{
        margin-top: -100px;
    }
    .title{
        margin: auto;
    }
    .modal-card-foot {
        width: 100%;
        margin:auto;
    }
</style>