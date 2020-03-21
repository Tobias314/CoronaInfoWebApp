<template>
  <body>
    <li v-for="item in themes" :key="item.id">
      <button @click="gotoinfo(item.link)"> 
        {{ item.name }}
      </button>
    </li>
  </body>
</template>

<script>

export default {
  name: 'Startpage',

  data: function() {
    return {
      themes: [
        {"name": "Persönliche Gesundheit", "id": 1, "link": "/medical"}, 
        {"name": "Rechtliche Informationen", "id": 2, "link": "/legal"},
        {"name": "Informationen zum Virus", "id": 3, "link": "/virus"},
        ],
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
