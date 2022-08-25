function choosecategory()
      {
        var category = document.getElementById("category");
        if(category.value == "staff")
        {
          // alert('success');
          document.getElementById("staff").style.display = "flex";
          document.getElementById("nonstaff").style.display = "none";
        }

        else if(category.value == "nonstaff")
        {
          document.getElementById("nonstaff").style.display = "flex";
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
          document.getElementById("bank").style.display = "flex";
          document.getElementById("display").style.display= "block"
          document.getElementById("personal").style.display = "none";
          document.getElementById("display2").style.display= "none"
        }

        else if(owner.value == "Personal")
        {
          document.getElementById("bank").style.display = "none";
          document.getElementById("display2").style.display= "block"
          document.getElementById("personal").style.display = "flex";
          document.getElementById("display").style.display= "none"
        }
        else
        {
          document.getElementById("bank").style.display = "none";
          document.getElementById("personal").style.display = "none";
        }
      }
      var row = 1;
      var add = document.getElementById('add');
      // add.addEventListener("click",display);

      

      function display()
      {
        var visitor_id= document.getElementById('visitor_id').value;
        var name = document.getElementById('name').value;
        var dest_dept= document.getElementById('dest_dept').value;
        var contact= document.getElementById('contact').value;
        var gadget_name=document.getElementById('gadget_name').value;
        var serial_number= document.getElementById('snumber').value;
        
        if(!visitor_id || !name || !dest_dept || !contact || !gadget_name || !serial_number)
        {
          alert("Please fill all the fields");
          return
        }

        var addrow = document.getElementById('show');
        var new_row = addrow.insertRow(row);

        var cel1 = new_row.insertCell(0);
        var cel2 = new_row.insertCell(1);
        var cel3 = new_row.insertCell(2);
        var cel4 = new_row.insertCell(3);
        var cel5 = new_row.insertCell(4);
        var cel6 = new_row.insertCell(5);
        var cel7 = new_row.insertCell(6);

        cel1.innerHTML = '<input type="text" value="'+visitor_id+'" name="visitor_id" class="form-control bg-light" style="border:0px; font-size: 15px; padding: 3px;"  />';
        cel2.innerHTML = '<input type="text" value="'+name+'" name="name" class="form-control bg-light" style="border:0px; font-size: 15px; padding: 3px;"  />';
        cel3.innerHTML = '<input type="text" value="'+dest_dept+'" name="dest_dept" class="form-control bg-light" style="border:0px; font-size: 15px; padding: 3px;"  />';
        cel4.innerHTML = '<input type="text" value="'+contact+'" name="contact" class="form-control bg-light" style="border:0px; font-size: 15px; padding: 3px;"  />';
        cel5.innerHTML = '<input type="text" value="'+gadget_name+'" name="gadget_name" class="form-control bg-light" style="border:0px; font-size: 15px; padding: 3px;"  />';
        cel6.innerHTML = '<input type="text" value="'+serial_number+'" name="serial_number" class="form-control bg-light" style="border:0px; font-size: 15px; padding: 3px;"  />';
        // cel7.innerHTML = '<a href="" id="btn"><i class="text-danger fa fa-trash" aria-hidden="true"></i></a>';
        row++;
        alert(row);

      }

      function displaystaff()
      {
        var employee_id= document.getElementById('employee_id').value;
        var bank_gadget = document.getElementById('bgadget_id').value;
        var bserial_number = document.getElementById('bserial_number').value;
        var personal_gadget= document.getElementById('pgadget_name').value;
        var serial_number= document.getElementById('serial_number').value;
        
        if(!employee_id)
        {
          alert("Please fill all the fields");
          return
        }

        var addrow = document.getElementById('show1');
        var addrow2 = document.getElementById('show2');
        var new_row = addrow.insertRow(row);
        var new_row2 = addrow2.insertRow(row);

        var cel1 = new_row.insertCell(0);
        var cel2 = new_row.insertCell(1);
        var cel3 = new_row.insertCell(2);
        var cel4 = new_row.insertCell(3);

        var cell1 = new_row2.insertCell(0);
        var cell2 = new_row2.insertCell(1);
        var cell3 = new_row2.insertCell(2);
        var cell4 = new_row2.insertCell(3);
        // var cel5 = new_row.insertCell(4);
        // var cel6 = new_row.insertCell(5);

        // cel1.innerHTML = employee_id;
        cel1.innerHTML = '<input type="text" value="'+employee_id+'" name="employee_id" class="form-control bg-light" style="border:0px;"  />';
        cel2.innerHTML = '<input type="text" value="'+bank_gadget+'" name="bank_gadget" class="form-control bg-light"  style="border:0px;"  />';
        cel3.innerHTML = '<input type="text" value="'+bserial_number+'" name="bserial_number" class="form-control bg-light" size="5" style="border:0px;"  />';
        cel4.innerHTML='<input type="checkbox" value="'+row+'" onchange="r()" id="row" name="row1" class="bg-light" size="5" checked />';

        cell1.innerHTML = '<input type="text" value="'+employee_id+'" name="employee_id" class="form-control bg-light" style="border:0px;"  />';
        cell2.innerHTML = '<input type="text" value="'+personal_gadget+'" name="personal_gadget" class="form-control bg-light" style="border:0px;"  />'
        cell3.innerHTML = '<input type="text" value="'+serial_number+'" name="serial_number" class="form-control bg-light" size="5" style="border:0px;"  />';
        cell4.innerHTML = '<input type="checkbox" value="'+row+'" onchange="r()" id="row" name="row" class="bg-light" size="5" checked/>';

        
        row++;
        var row_list=[];
        for (var i=1;i<row;i++)
        {
          if(document.getElementById('row').checked == 1)
          {
            row_list.push(i);
          }
          // alert(row_list);
        }

        document.getElementById('output').value = row_list;
        
      }
      
      