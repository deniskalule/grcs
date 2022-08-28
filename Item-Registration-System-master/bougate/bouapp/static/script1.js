function choosecategory()
      {
        var category = document.getElementById("category");
        if(category.value == "staff")
        {
          // alert('success');
          document.getElementById("staff").style.display = "block";
          document.getElementById("nonstaff").style.display = "none";
        }

        else if(category.value == "nonstaff")
        {
          document.getElementById("nonstaff").style.display = "block";
          document.getElementById("staff").style.display = "none";
        }
        else
        {
          document.getElementById("staff").style.display = "none";
          document.getElementById("nonstaff").style.display = "none";
        }
      }

      function chooseowner()
      {
        var owner = document.getElementById("gadget_owner");
        if(owner.value == "Bank")
        {

          // alert('success');
          document.getElementById("bank").style.display = "block";
          // document.getElementById("display").style.display= "block"
          document.getElementById("personal").style.display = "none";
          // document.getElementById("display2").style.display= "none"
        }

        else if(owner.value == "Personal")
        {
          document.getElementById("bank").style.display = "none";
          // document.getElementById("display2").style.display= "block"
          document.getElementById("personal").style.display = "block";
          // document.getElementById("display").style.display= "none"
        }
        else
        {
          document.getElementById("bank").style.display = "none";
          document.getElementById("personal").style.display = "none";
        }
      }

      function searchfunction()
    {
        const searchinput = document.getElementById("search").value.toUpperCase();
        const ptable = document.getElementById("product-table");
        const store = document.getElementById("body");
        const product = document.querySelectorAll(".product");
        const item = document.getElementsByTagName('td');
        const pname = document.getElementsByTagName("h6");

        for(var i = 0 ;i < pname.length; i++)
        {
            let match = product[i].getElementsByTagName('h6')[0];

            if(match)
            {
                let textValue = match.textContent || match.innerHTML;

                if(textValue.toUpperCase().indexOf(searchinput) > -1)
                {
                    product[i].style.display = "";

                }

                else
                {
                  product[i].style.display = "none";
                }
            }
        }
    }
    function search()
    {
        const searchinput = document.getElementById("search2").value.toUpperCase();
        const ptable = document.getElementById("product-table2");
        const store = document.getElementById("body2");
        const product = document.querySelectorAll(".product2");
        const item = document.getElementsByTagName('td');
        const pname = document.getElementsByTagName("h6");

        for(var i = 0 ;i < pname.length; i++)
        {
            let match = product[i].getElementsByTagName('h6')[0];

            if(match)
            {
                let textValue = match.textContent || match.innerHTML;

                if(textValue.toUpperCase().indexOf(searchinput) > -1)
                {
                    product[i].style.display = "";

                }

                else
                {
                  product[i].style.display = "none";
                }
            }
        }
    }
    
      
      