$(document).ready(function() {
    $(".content").css("height", $(window).height() + "px");
});


$.widget( "custom.catcomplete", $.ui.autocomplete, {
    _create: function() {
      this._super();
      this.widget().menu( "option", "items", "> :not(.ui-autocomplete-category)" );
    },
    _renderMenu: function( ul, items ) {
      var that = this,
        currentCategory = "";
      $.each( items, function( index, item ) {
        var li;
        if ( item.category != currentCategory ) {
          ul.append( "<li class='ui-autocomplete-category'>" + item.category + "</li>" );
          currentCategory = item.category;
        }
        li = that._renderItemData( ul, item );
        if ( item.category ) {
          li.attr( "aria-label", item.category + " : " + item.label );
        }
      });
    }
  });

$(function() {
  var data = [
    { label: "Make a journal entry", category: "Journaling" },
    { label: "Create an activity", category: "Journaling" },
    { label: "Ask my coordinator something", category: "Forums" },
    { label: "Ask my coordinator something", category: "Forums" },
  ];

  $( "#search" ).catcomplete({
    delay: 0,
    source: data
  });
});
