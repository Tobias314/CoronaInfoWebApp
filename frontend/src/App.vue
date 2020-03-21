<template>
  <body>
    <header>
      <h2 @click="gotoStart()">
        Corona-Informationen
      </h2>
    </header>
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

  methods: {
    gotoStart: function(){
      this.$router.push("/")
    },
  },
}
</script>

<style>

</style>
