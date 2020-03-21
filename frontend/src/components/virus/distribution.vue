<template>
  <body>
     Exponentiell. Ja, Oma, das ist sehr schnell.
     {{ this.$parent.location }}
     {{casecount}}
  </body>
</template>

<script>
import Api from "../api.js";

export default {
  name: 'general_info',

  data:function(){
    return{
      casecount: "",
    }
  },

  mounted(){
    Api.get(`/district_case_number/${this.$parent.location}`)
    .then(response => {
      this.casecount = response.data;
    }, error => {
      console.error(error);
    });
  }
}
</script>

<style>

</style>
