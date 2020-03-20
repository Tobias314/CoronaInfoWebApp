<template>
  <body>
     <li v-for="item in themes" :key="item.id">
    {{ item.name }}
    </li>
  </body>
</template>

<script>

export default {
  name: 'App',

  data: function() {
    return {
      themes: [{"name": "help me vllt habe ich corona", "id": 1}, {"name": "lol ich bin broke", "id": 2}, {"name": "wo bekomme ich gute wissenschaftliche infos?", "id": 3}],
    }
  }
}
</script>

<style>

</style>
