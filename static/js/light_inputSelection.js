 $("form input[type=submit]").click(function() {
        $("input[type=submit]", $(this).parents("form")).removeAttr("clicked");
        $(this).attr("clicked", "true");
    });

    $('form[name=lights]').submit(function(){
        var val = $("input[type=submit][clicked=true]").attr("name");
        var serial = $(this).serialize();
        if (serial === "")
            serial = val+"="+val;
        else
            serial += "&"+val+"="+val;
        $.post($(this).attr('action'), serial, function(res){
            //console.log(res);
        });
        return false;

    });

    $('#resetFields').click(function(){
        $('#color_me1').prop('selectedIndex',0).css("background-color", "white");
        $('#color_me2').prop('selectedIndex',0).css("background-color", "white");
        $('#color_me3').prop('selectedIndex',0).css("background-color", "white");
        $('#color_me4').prop('selectedIndex',0).css("background-color", "white");
    });

    $("#color_me1").change(function(){
        var selectedOption = this.selectedOptions[0]
        var color = selectedOption.style.backgroundColor
        $("#color_me1").css("background-color", color);
    });
    $("#color_me2").change(function(){
        var selectedOption = this.selectedOptions[0]
        var color = selectedOption.style.backgroundColor
        $("#color_me2").css("background-color", color);
    });
    $("#color_me3").change(function(){
        var selectedOption = this.selectedOptions[0]
        var color = selectedOption.style.backgroundColor
        $("#color_me3").css("background-color", color);
    });
    $("#color_me4").change(function(){
        var selectedOption = this.selectedOptions[0]
        var color = selectedOption.style.backgroundColor
        $("#color_me4").css("background-color", color);
    });