$(document).ready(function(){
    let $base_form = $(".dynamically-repeated").first();
    let $append_div = $("#dynamic");
    let $add_button = $("#add_form");
    let $remove_button = $("#remove_form");

    const min_entries = 1;
    let current_entries = $append_div.children().length;

    if (current_entries == min_entries)
        $remove_button.addClass("disabled");

    function update_form_count()
    {
        $("#form_count").text(current_entries);
    }

    $add_button.click(function(){
        let $new_form = $base_form.clone();

        let $inputs = $new_form.find("input");
        $inputs.each(function(index){
            let current_id = $($inputs[index]).attr("id");
            if (current_id == undefined)
                return;
            let elem_name = current_id.split("-").splice(2).join("-");
            if (elem_name == "")
                return;

            let new_id = "per_entry_params-" + current_entries + "-" + elem_name;
            $($inputs[index]).attr("id", new_id);
            $($inputs[index]).attr("name", new_id);
        });

        let $selects = $new_form.find("select");
        $selects.each(function(index){
            let current_id = $($selects[index]).attr("id");
            if (current_id == undefined)
                return;
            let elem_name = current_id.split("-").splice(2).join("-");
            if (elem_name == "")
                return;

            let new_id = "per_entry_params-" + current_entries + "-" + elem_name;
            $($selects[index]).attr("id", new_id);
            $($selects[index]).attr("name", new_id);
        });

        $new_form.appendTo($append_div);

        current_entries++;
        update_form_count();

        $remove_button.removeClass("disabled");
    });

    $remove_button.click(function(){
        if (current_entries > min_entries)
        {
            $append_div.children().last().remove();
            current_entries--;
            update_form_count();

            if (current_entries == min_entries)
                $remove_button.addClass("disabled");
        }
    });
});
