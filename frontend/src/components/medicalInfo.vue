<template>
  <body>
    <div>insert medical info here</div>

    <a :href="'//' + 'covapp.charite.de/questionaire'" target="_blank">
      Quiz vom Charite
    </a>

    <div> {{gesundheitsamt}} </div>
  </body>
</template>

<script>
import Api from "./api.js";

export default {
  name: 'medical info',

  data: function(){
    return {
      gesundheitsamt: 1111,
    }
  },

  mounted(){
    Api.get(`phone_number/gesundheitsamt/Potsdam`)
    .then(response => {
      this.gesundheitsamt = response.data;
    }, error => {
      console.error(error);
    });
  },


  


}
</script>

<style>

</style>