<template>

<div class="column">
    <div class="box">
            <figure class="image is-128x128  mb-4 ">
                    <img class="is-rounded" v-bind:src="review.get_photo">
                </figure>
            <h3 class="is-size-5">{{ review.name }}</h3>
            
            <p class="is-size-6 text-review">{{ review.review }}</p>
             
    </div>
</div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Reviews',
    props:{
        review:Object,
    }
}
</script>
<style scoped>
    .box {
        height: 100%;
        box-shadow: rgba(0, 0, 0, 0.45) 10px 10px 20px -5px;
        border-radius: 7px;
        border: none;
        padding:40px;
        background: white;
    }
    .image{
        margin: auto;
    }
    h3{
        text-align: center;
        font-family: 'Lato Regular';
        
           }
    p{
        text-align: center;
        font-family: 'Lato Light';
        
    }
    .text-review{
        padding-top: 10px;
        padding-bottom: 5px;
        
    }
</style>