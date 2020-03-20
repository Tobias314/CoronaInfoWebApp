<template>
  <body>
    All the Corona Infos you need
    <li v-for="item in themes" :key="item.id">
      <button @click="gotoinfo(item.link)"> 
        {{ item.name }}
      </button>
    </li>
  </body>
</template>

<script>

export default {
  name: 'App',

  data: function() {
    return {
      themes: [{"name": "help me vllt habe ich corona", "id": 1, "link": "/medical"}, {"name": "lol ich bin broke", "id": 2, "link": "/legal"}],
    }
  },

  methods: {
    gotoinfo: function(link){
      this.$router.push(link); 
    }
  },


}
</script>

<style>

</style>
