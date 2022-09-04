<template>
  <div class="my-page">
    <div class="blur-wrapper">
  <div class="hero is-fullheight catalog">
    <div class="columns is-multiline is-parent cat">
          <div class="column is-12">
            <h2 class="is-size-2 has-text-centered">Каталог</h2>
          </div>
          <div class="filter column is-2">
            <div class="box">
              <form class="fil">
                <h1 class="has-text-centered"><b> Фильтр</b></h1>
                
                <p><h4>Основа: </h4></p>
                <p><input type="checkbox" value="4" v-model="selectedChecks"><label> Безе</label></p>
                <p><input type="checkbox" value="2" v-model="selectedChecks"><label> Бисквит</label></p>
                <p><input type="checkbox" value="3" v-model="selectedChecks"><label> Песочное</label></p>
                <p><input type="checkbox" value="1" v-model="selectedChecks"><label> Суфле</label></p>
                <p><input type="checkbox" value="5" v-model="selectedChecks"><label> Чизкейк</label></p>
                <p><input type="checkbox" value="6" v-model="selectedChecks"><label> Слоеное</label></p>
                <p><h4>Вкус: </h4></p>
                <p><input type="checkbox" value="1" v-model="selectedChecks2"><label> Ванильный</label></p>
                <p><input type="checkbox" value="6" v-model="selectedChecks2"><label> Кофейный</label></p>
                <p><input type="checkbox" value="5" v-model="selectedChecks2"><label> Ореховый</label></p>
                <p><input type="checkbox" value="4" v-model="selectedChecks2"><label> Фруктовый</label></p>
                <p><input type="checkbox" value="2" v-model="selectedChecks2"><label> Шоколадный</label></p>
                <p><input type="checkbox" value="3" v-model="selectedChecks2"><label> Ягодный</label></p>
                <div class="control">
                  <a class="button" @click='getFiltered(selectedChecks, selectedChecks2)'>Применить</a>
                </div>

              </form>
            </div>

          </div>
          <div class="products column is-10">
            <div class="columns is-multiline">
          <ProductBox 
                v-for="product in getProduct"
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
  name: 'Catalog',
  data(){
    return{
      getProduct: [],
      selectedChecks:[],
      selectedChecks2:[],
    }
  },
  components: {
    ProductBox,
  },
  mounted(){
    this.getProducts()
    document.title = 'Catalog | MoonPie'


  },
  methods:{
    getProducts(){
      axios
        .get('/api/v1/getProduct/')
        .then(response =>{
          this.getProduct = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    async getFiltered(checks, checks2){
      this.$store.commit('setIsLoading', true)
      await axios
      .post('/api/v1/getFilter/', {'checks':this.selectedChecks, 'checks2':this.selectedChecks2})
      .then(response =>{
          this.getProduct = response.data
          
        })
        .catch(error => {
          console.log(error)
        })
    this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style scoped>
.catalog{
  padding-top:80px;
  font-family:'Gotham Pro';
}

.cat{
  padding: 50px;
  background-color: rgb(255, 247, 242);
}
h2{
  margin-top:-20px;
}

h4{
  padding-top: 10px;
  padding-bottom:10px;
}
.button{
  color:antiquewhite;
        border-radius: 3px;
        background-color: #201d1cbb;
        padding:10px;
        
        margin-top: 20px;
}
.control{
  text-align: center;
}
.filter{
  
}
.product-list{
  
}
</style>