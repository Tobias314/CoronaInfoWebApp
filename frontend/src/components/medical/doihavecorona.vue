<template>
  <body>
    <a :href="'//' + 'covapp.charite.de/questionaire'" target="_blank">
      Quiz vom Charite
    </a>
  </body>
</template>

<script>
import Api from "../api.js";

export default {
  name: 'medical_info',

  data: function(){
    return {
      gesundheitsamt: 1111,
    }
  },

  mounted(){
    Api.get(`phone_number/health_department/Potsdam`)
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