<!DOCTYPE html>
<html lang="en">>
    <head>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }

            table, td, th {
                border: 1px solid black;
                padding: 5px;
            }

            th {text-align: left;}
        </style>
    </head>
<body>
    <!-- <div class="jumbotron jumbotron-fluid">
        <div class="container">
            <h1 class="display-4">Alert Level $alert_level</h1>
            <p class="lead">Alert Level</p>
        </div>
    </div>  -->
    <?php
        echo "<html><body><table>\n\n";
        $f = fopen("scoredData.csv", "r");
        while (($line = fgetcsv($f)) !== false) {
            echo "<tr>";
            $counter_int = 0;
            $num_cols = 5;
            $alert_level = 0;
            foreach ($line as $cell) {
                if ($counter_int == 0) {
                    if (htmlspecialchars($cell) == '1') {
                        echo "<td bgcolor=\"#00FF00\">" . htmlspecialchars($cell) . "</td>";
                        $alert_level = 1;
                    }
                    else if (htmlspecialchars($cell) == '2') {
                        echo "<td bgcolor=\"#FFFF00\">" . htmlspecialchars($cell) . "</td>";
                        $alert_level = 2;
                    }
                    else if (htmlspecialchars($cell) == '3') {
                        echo "<td bgcolor=\"#FF0000\">" . htmlspecialchars($cell) . "</td>";
                        $alert_level = 3;
                    }
                    else {
                        echo "<td>" . htmlspecialchars($cell) . "</td>";
                    }
                }
                else {
                    echo "<td>" . htmlspecialchars($cell) . "</td>";
                }
                $counter_int += 1;
            }
            echo "</tr>\n";
        }
       
        
        echo "\n</table></body></html>";


    ?>
</body>
</html>