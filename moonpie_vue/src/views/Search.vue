<template>
<div class="my-page">
    <div class="blur-wrapper">
    <div class="hero is-fullheight page-search">
        <div class="hero is-fullheight columns is-multiline search">
            <div class="column is-12">
                <h1 class="is-size-3 has-text-centered"> Поиск </h1>
                <h2 class="is-size-5 has-text-grey"> Результаты поиска по запросу "{{ query }}":</h2>

            </div>
           <div class="products column is-12">
            <div class="columns is-multiline">
            <ProductBox
                v-for="product in products"
                v-bind:key="product.id"
                v-bind:product="product"/>
            </div>
           </div>
        </div>
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'
export default {
    name: 'Search',
    components:{
        ProductBox
    },
    data(){
        return{
            products:[],
            query:''
        }
    },
    mounted(){
        document.title = 'Search | MoonPie'
        
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')){
            this.query = params.get('query')
            this.performSearch()
            
        }
    },
    methods:{
        async performSearch(){
            this.$store.commit('setIsLoading',true)
        await axios
                .post('/api/v1/products/search/',{'query':this.query})
                .then(response=>{
                    this.products = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading',false)

        }
    }
}
</script>
<style scoped>
.page-search{
    font-family:'Gotham Pro';
    padding-top:80px;
}
.search{
    padding: 50px;
    padding-top: 30px;
    background-color: rgb(255, 247, 242);
}
</style>