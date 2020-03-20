<template>
  <body>
     <li v-for="item in themes" :key="item.id">
    {{ item.name }}
    <button @click="gotoinfo(item.id)"> go to info </button>
    </li>
  </body>
</template>

<script>

export default {
  name: 'App',

  data: function() {
    return {
      themes: [{"name": "help me vllt habe ich corona", "id": 1}, {"name": "lol ich bin broke", "id": 2}],
    }
  },

  methods: {
    gotoinfo: function(id){
      switch(id){
        case 1: this.$router.push("/medical");
                break;
        case 2: this.$router.push("/legal");
                break;
        default: break;
      }
    }
  },


}
</script>

<style>

</style>
