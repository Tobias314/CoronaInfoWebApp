<template>
  <body>
    <div class="full-control">
      <div class="list">

        <md-list v-for="item in themes" :key="item.id">
          <md-list-item md-expand :md-expanded.sync="item.expand">
            <span class="md-list-item-text">{{item.name}}</span>

            <md-list slot="md-expand">
              <md-list-item class="md-inset" v-for="subtopic in item.subtopics" :key="subtopic.id" @click=gotoinfo(subtopic.link)>
                {{ subtopic.name }}
              </md-list-item>
            </md-list>
          </md-list-item>

        </md-list>
        <md-list-item @click="gotoinfo(stupid_vue)">
          FAQ
        </md-list-item>
      </div>
  </div>

  </body>
</template>

<script>

export default {
  name: 'Startpage',

  data: function() {
    return {
      themes: [
        {name: "Persönliche Gesundheit", id: 1, expand: false, subtopics: [
                                                                {name: "Wo bekomme ich Hilfe bei psychischen Problemen?", id: 13, link: "/mentalhealth"},
                                                                {name: "Wo kann ich mich testen lassen?", id: 14, link: "/testing"}]},
        {name: "Rechtliche Informationen", id: 2, expand: false, subtopics: [
                                                                {name: "Darf ich noch raus?", id: 21, link: "/stayhome"}, 
                                                                {name: "Woher bekomme ich finanzielle Unterstützung?", id: 22, link: "/finances"}]}, 
        {name: "Informationen zum Virus", id: 3, expand: false, subtopics: [
                                                                {name: "Wie ist die Ausbreitung?", id: 33, link: "/distribution"}]},
        {name: "Allgemein", id: 41, expand: false, subtopics: [
            {name: "Habe ich Corona?", id: 42, link: "/doihavecorona"},
            {name: "Was ist das für ein Virus?", id: 43, link: "/virus"},
            {name: "Was wird aktuell geforscht?", id: 44, link: "/research"},
            {name: "Ich habe Corona, was sollte ich tun?", id: 45, link: "/coronaandnow"},

          ]},
        ],
        stupid_vue : '/faq'
        // Nachbarschafts Hilfe wo bekommen, wo anbieten?
        // News
    }
  },

  methods: {
    gotoinfo: function(link){
      this.$router.push(link);
    }
  },


}
</script>

<style lang="scss" scoped>
  $list-width: 100%;

  .full-control {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap-reverse;
  }

  .list {
    width: $list-width;
  }

  .md-list {
    width: 100%;
    max-width: 100%;
    display: inline-block;
  }

  .full-control > .md-list {
    width: $list-width;
    max-width: 100%;
    height: 400px;
    display: inline-block;
    overflow: auto;
    border: 1px solid rgba(#000, .12);
    vertical-align: top;
  }

  .control {
    min-width: 250px;
    display: flex;
    flex-direction: column;
    padding: 16px;
  }
</style>