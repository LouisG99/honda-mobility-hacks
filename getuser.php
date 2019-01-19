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

    <?php
        echo "<html><body><table>\n\n";
        $f = fopen("test.csv", "r");
        while (($line = fgetcsv($f)) !== false) {
                echo "<tr>";
                foreach ($line as $cell) {
                        echo "<td>" . htmlspecialchars($cell) . "</td>";
                }
                echo "</tr>\n";
        }
        fclose($f);
        echo "\n</table></body></html>";
    ?>
</body>
</html>