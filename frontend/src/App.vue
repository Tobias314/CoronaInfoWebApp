<template>
  <body>
     <main>
      <transition name="component-fade" mode="out-in">
        <router-view />
      </transition>
    </main>
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
